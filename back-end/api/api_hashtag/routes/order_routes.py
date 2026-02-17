from fastapi import APIRouter, Depends, HTTPException
import sys
import os
from schemas.schemas import OrderSchema, ItemOrderSchema
from sqlalchemy.orm import Session
from routes.dependencies.dependencies import pegar_sessao, verificar_token
from models.models import Order, Usuario, ItemOrder

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
)

order_router = APIRouter(prefix="/orders", tags=["orders"], dependencies = [Depends(verificar_token)])

@order_router.get("/")
async def home():
    return {"messege": "Voce acessou a rota padrao de pedidos."}

@order_router.post("/create_order")
async def new_order(order_schema : OrderSchema, session : Session = Depends(pegar_sessao)):
    new_order = Order(id= None, usuario = order_schema.usuario, status = None)
    session.add(new_order)
    session.commit()
    return {"message" : f"Novo pedido criado. ID PEDIDO: {new_order.id}"}

@order_router.post("/cancel/{id_pedido}")
async def cancel_order(id_pedido: int, session : Session = Depends(pegar_sessao), usuario : Usuario = Depends(verificar_token)):
    pedido = session.query(Order).filter(id_pedido==Order.id).first()
    if not pedido:
        raise HTTPException(status_code=400, detail='no orders found')
    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=401, detail='Unauthorized user')
    if pedido.status == 'CANCELADO':
        raise HTTPException(status_code=400, detail='This order has already been cancelled')
    pedido.status = 'CANCELADO'
    session.commit()
    return{
        'message': f'order ID: {pedido.id} successfully canceled',
        'pedido': pedido
    }
    
@order_router.get("/order_list")
async def order_list(session : Session = Depends(pegar_sessao), usuario : Usuario = Depends(verificar_token)):
    pedido = session.query(Order).all()
    if not pedido:
        raise HTTPException(status_code=400, detail='no orders found')
    if not usuario.admin:
        raise HTTPException(status_code=401, detail='Unauthorized user')
    return {
        'message': f'{len(pedido)} requests found',
        'pedidos': pedido
    }
    
@order_router.post("/add_item/{id_pedido}")
async def add_item(id_pedido: int, item_pedido_schema: ItemOrderSchema, session : Session = Depends(pegar_sessao), usuario : Usuario = Depends(verificar_token)):
    pedido = session.query(Order).filter(Order.id == id_pedido).first()
    if not pedido:
        raise HTTPException(status_code=400, detail='no orders found')
    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=401, detail='Unauthorized user')
    item_pedido = ItemOrder(None, id_pedido, item_pedido_schema.sabor, item_pedido_schema.preco_unitario, item_pedido_schema.quantidade, item_pedido_schema.tamanho)
    session.add(item_pedido)
    pedido.calc_preco()
    session.commit()
    return {
        "message": "Novo item adicionado com sucesso",
        "id item": item_pedido.id,
        "preço unitario": item_pedido.preco_unitario
    }
    
@order_router.post("/delete_item/{id_item_pedido}")
async def delete_item(id_item_pedido: int, session : Session = Depends(pegar_sessao), usuario : Usuario = Depends(verificar_token)):
    item_pedido = session.query(ItemOrder).filter(ItemOrder.id == id_item_pedido).first()
    pedido = session.query(Order).filter(item_pedido.pedido == Order.id).first()
    if not pedido:
        raise HTTPException(status_code=400, detail='no orders found')
    if not usuario.admin and usuario.id != pedido.usuario:
        raise HTTPException(status_code=401, detail='Unauthorized user')
    session.delete(item_pedido)
    pedido.calc_preco()
    session.commit()
    return {
        "message": f"Item {item_pedido.id} excluido com sucesso.",
        "Itens pedido": len(pedido.itens),
        "pedido": pedido
    }
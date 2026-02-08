from fastapi import APIRouter, Depends
import sys
import os
from schemas.schemas import OrderSchema
from sqlalchemy.orm import Session
from routes.dependencies.dependencies import pegar_sessao
from models.models import Order

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
)

order_router = APIRouter(prefix="/orders", tags=["orders"])

@order_router.get("/")
async def home():
    return {"messege": "Voce acessou a rota padrao de pedidos."}

@order_router.post("/order")
async def new_order(order_schema : OrderSchema, session : Session = Depends(pegar_sessao)):
    new_order = Order(id= None, usuario = order_schema.usuario, status = None)
    session.add(new_order)
    session.commit()
    return {"message" : f"Novo pedido criado. ID PEDIDO: {new_order.id}"}
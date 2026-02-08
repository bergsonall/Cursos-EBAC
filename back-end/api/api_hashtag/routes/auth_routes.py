from fastapi import APIRouter, Depends
import sys
import os
from main import bcrypt_context
from models.models import Usuario 
from routes.dependencies.dependencies import pegar_sessao
from schemas.schemas import UsuarioSchema
from sqlalchemy.orm import Session 

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
)

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    return {"messege": "Voce acessou a rota padrao de autenticação."}

@auth_router.post("/criar_conta")
async def criar_conta(usuario_schema : UsuarioSchema, session : Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email == usuario_schema.email).first()
    if usuario:
        return {"message" : "Usuario já cadastrado"}
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_criptografada, usuario_schema.ativo, usuario_schema.admin)
        session.add(novo_usuario)
        session.commit()
        return {"message" : "Sua conta foi criada com sucesso"}
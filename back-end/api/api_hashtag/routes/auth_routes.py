from fastapi import APIRouter, Depends
import sys
import os
from main import bcrypt_context
from models.models import Usuario 
from routes.dependencies.dependencies import pegar_sessao

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
)

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    return {"messege": "Voce acessou a rota padrao de autenticação."}

@auth_router.post("/criar_conta")
async def criar_conta(nome : str, email : str, senha : str, session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email == email).first()
    if usuario:
        return {"message" : "Usuario já cadastrado"}
    else:
        senha_criptografada = bcrypt_context.hash(senha)
        novo_usuario = Usuario(id=None, nome=nome, email=email, senha=senha_criptografada)
        session.add(novo_usuario)
        session.commit()
        return {"message" : "Sua conta foi criada com sucesso"}
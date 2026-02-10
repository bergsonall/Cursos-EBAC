from fastapi import APIRouter, Depends, HTTPException
import sys
import os
from main import bcrypt_context, ACCESS_TOKEN_EXPIRE_MINUTE, ALGORITHM, SECRET_KEY
from models.models import Usuario 
from routes.dependencies.dependencies import pegar_sessao, verificar_token
from schemas.schemas import UsuarioSchema, LoginSchema
from sqlalchemy.orm import Session 
from jose import jwt, JWTError
from datetime import timedelta, datetime, timezone

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
)

def criar_token(id_usuario, duracao_token = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTE)):
    expira = datetime.now(timezone.utc) + duracao_token
    dic_info = {"sub": id_usuario, "exp": expira}
    encoded_jwt = jwt.encode(dic_info, SECRET_KEY, ALGORITHM)
    return encoded_jwt

def autenticar_usuario(email, senha, session):
    usuario = session.query(Usuario).filter(Usuario.email == email).first()
    if not usuario:
        return False
    elif not bcrypt_context.verify(senha, usuario.senha):
        return False
    return usuario
        

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    return {"messege": "Voce acessou a rota padrao de autenticação."}

@auth_router.post("/create_account")
async def criar_conta(usuario_schema : UsuarioSchema, session : Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email == usuario_schema.email).first()
    if usuario:
        raise HTTPException(status_code=400, detail="Email já cadastrado.")
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(None, usuario_schema.nome, usuario_schema.email, senha_criptografada, usuario_schema.ativo, usuario_schema.admin)
        session.add(novo_usuario)
        session.commit()
        return {"message" : "Sua conta foi criada com sucesso"}
    
@auth_router.post("/login")
async def login(login_schema : LoginSchema, session : Session = Depends(pegar_sessao)):
    usuario = autenticar_usuario(login_schema.email, login_schema.senha, session)
    if not usuario:
        raise HTTPException(status_code=400, detail="Email não cadastrado.")
    else:
        access_token = criar_token(usuario.id)
        refresh_token = criar_token(usuario.id, duracao_token=timedelta(days=7))
        return {
            "access_token" : access_token,
            "refresh_token" : refresh_token,
            "token_type" : "Bearer"
        }
        
@auth_router.get("/refresh")
async def use_refresh_token(usuario: Usuario = Depends(verificar_token)):
    access_token = criar_token(usuario.id)
    return {
            "access_token" : access_token,
            "token_type" : "Bearer"
        }
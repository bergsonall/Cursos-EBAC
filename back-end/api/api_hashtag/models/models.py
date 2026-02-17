from typing import Optional
from sqlalchemy import create_engine, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

# Cria conexao com o banco de dados
db = create_engine("sqlite:///database/banco.db")

# Cria a base do banco de dados
class Base(DeclarativeBase):
    pass

# Cria as classes/tabelas do banco de dados
class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[Optional[str]] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, nullable=False)
    senha: Mapped[Optional[str]] = mapped_column(String)
    ativo: Mapped[bool] = mapped_column(Boolean, default=True)
    admin: Mapped[bool] = mapped_column(Boolean, default=False)
    
    def __init__(self, id, nome, email, senha, ativo=True, admin=False):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin
        
        
class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    status: Mapped[str] = mapped_column(String, nullable=False, default="PENDENTE")
    usuario: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("usuarios.id"))
    preco: Mapped[Optional[float]] = mapped_column(Float)
    itens = relationship("ItemOrder", cascade="all, delete")
    
    def __init__(self, id, status, usuario, preco=0):
        self.id = id
        self.status = status
        self.usuario = usuario
        self.preco = preco
        
    def calc_preco(self):
        self.preco = sum(item.quantidade * item.preco_unitario for item in self.itens)
        
        
class ItemOrder(Base):
    __tablename__ = 'itens_order'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    pedido: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("orders.id"))
    sabor: Mapped[Optional[str]] = mapped_column(String)
    preco_unitario: Mapped[Optional[float]] = mapped_column(Float)
    quantidade: Mapped[Optional[int]] = mapped_column(Integer)
    tamanho: Mapped[Optional[str]] = mapped_column(String)
    
    def __init__(self, id, pedido, sabor, preco_unitario, quantidade, tamanho):
        self.id = id
        self.pedido = pedido
        self.sabor = sabor
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade
        self.tamanho = tamanho
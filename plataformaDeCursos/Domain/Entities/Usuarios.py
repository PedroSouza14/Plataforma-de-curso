from sqlalchemy import Column, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

base_usuarios = declarative_base()

class Usuarios(base_usuarios):
    __tablename__ = 'Usuarios'

    Cpf = Column (String(11), primary_key=True, autoincrement=False)
    Email = Column (String(150),nullable=False )
    Nome = Column (String(200), nullable=False)
    Senha = Column (String, nullable=False)
    Banido = Column (Boolean, default=False)

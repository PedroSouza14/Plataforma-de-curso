from sqlalchemy import Column, String,Boolean
from sqlalchemy.ext.declarative import declarative_base
base_administradores = declarative_base()

class administradores(base_administradores):
    __tablename__ = 'Administradores'
    Cpf = Column (String(11), primary_key=True)
    Email = Column (String(150), nullable=True)
    Nome = Column (String(200),nullable=True)
    Senha = Column (String, nullable=True)
    Banido = Column (Boolean, default=False)
    

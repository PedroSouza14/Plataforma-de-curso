from sqlalchemy import Column, String,Integer,Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
base_cursos = declarative_base()

class Cursos(base_cursos):
    __tablename__ = 'Cursos'

    CursoId = Column (Integer,primary_key=True)
    Nome = Column (String(100),nullable=True)
    Descricao = Column (String(200))
    DataPublicacao = Column (Date,default=datetime.today())
    Disponivel = Column(Boolean, default=True)
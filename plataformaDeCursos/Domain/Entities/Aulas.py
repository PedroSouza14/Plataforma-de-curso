from sqlalchemy import Column,String, ForeignKey, Integer, Time
from sqlalchemy.ext.declarative import declarative_base
from Domain.Entities.Cursos import Cursos
from datetime import datetime

base_aulas = declarative_base()

class Aulas(base_aulas):
    __tablename__= 'Aulas'
    AulaId = Column (Integer, primary_key=True, autoincrement=True)
    CursoId = Column (Integer, ForeignKey(Cursos.CursoId))
    Nome = Column (String (100), nullable=True)
    Descricao = Column (String(200), nullable=True)
    Complemento = Column (String, nullable=True)
    Duracao = Column(Time, nullable=True)
    Data_publicacao = Column(datetime, nullable=False)
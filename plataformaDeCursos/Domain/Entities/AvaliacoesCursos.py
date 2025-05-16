from sqlalchemy import Column, String, ForeignKey, Date, Enum, Integer
from sqlalchemy.ext.declarative import declarative_base
from Domain.Entities.Cursos import Cursos
from Domain.Entities.Usuarios import Usuarios
from datetime import datetime
import enum


base_avaliacoes_cursos = declarative_base()

class AvaliacaoEnum (enum.Enum):
    muito_ruim = 1
    ruim = 2
    regular = 3
    bom = 4
    muito_bom = 5


class avaliacoes_cursos(base_avaliacoes_cursos):
    __tablename__ = 'AvaliacoesCursos'

    CursoId = Column (String(36),ForeignKey(Cursos.CursoId), primary_key=True, autoincrement=False)
    Cpf = Column (String (11), ForeignKey(Usuarios.Cpf), primary_key=True, autoincrement=False)
    Opniao = Column (String(250))
    Avaliacao = Column (Enum(AvaliacaoEnum))
    DataAvaliacao = Column (Date, default=datetime.today())
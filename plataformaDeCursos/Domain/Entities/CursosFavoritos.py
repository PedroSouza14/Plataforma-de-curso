from sqlalchemy import Column,String, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from Domain.Entities.Cursos import Cursos
from Domain.Entities.Usuarios import Usuarios
base_cursos_favoritos = declarative_base()

class CursosFavoritos(base_cursos_favoritos):
    __tablename__= 'CursosFavoritos'
    
    Cpf = Column (String(11),ForeignKey(Usuarios.Cpf), primary_key=True, autoincrement=False)
    Curso = Column (Integer, ForeignKey(Cursos.CursoId), primary_key=True, autoincrement=False)
    

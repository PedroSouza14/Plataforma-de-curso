from Infrastructure.Connection.CursosContext import dbcursos
from Domain.Entities.Cursos import Cursos

def get_all_cursos():
    with dbcursos() as session:
        return session.query(Cursos).filter(Cursos.Disponivel == True).all()

def get_cursos_by_cursoid(curso_id: int):
    with dbcursos() as session:
        return session.query(Cursos).filter(Cursos.CursoId == curso_id).first()

def create_cursos(Curso: Cursos):
    with dbcursos() as session:
        session.add(Curso)
        session.commit()

def update_cursos(curso_id: int, Curso: Cursos):
    with dbcursos() as session:
        curso_entity = session.query(Cursos).filter(Cursos.CursoId == curso_id).first()
        curso_entity.Nome = Curso.Nome
        curso_entity.Descricao = Curso.Descricao
        session.commit()

def delete_cursos(curso_id: int):
    with dbcursos() as session:
        curso_entity = session.query(Cursos).filter(Cursos.CursoId == curso_id).first()
        condicao_disponivel = False if curso_entity.Disponivel == False else True
        curso_entity.Disponivel = condicao_disponivel
        session.commit()

from Infrastructure.Connection.CursosContext import dbcursos
from Domain.Entities.CursosFavoritos import CursosFavoritos
from Domain.Entities.Usuarios import Usuarios

def get_all_cursos_favoritados_by_cpf(cpf: str):
    with dbcursos() as session:
        return session.query(CursosFavoritos).filter(CursosFavoritos.Cpf == cpf).all()

def Adicionar_cursos(CursosFavoritos:CursosFavoritos):
    with dbcursos() as session:
        session.add(CursosFavoritos)
        session.commit()

def remover_curso_favorito(cpf: str, curso_id: int):
    with dbcursos() as session:
        curso_favorito = session.query(CursosFavoritos).filter (CursosFavoritos.Cpf == cpf and CursosFavoritos.Curso == curso_id).first()
        if curso_favorito:
            session.delete(curso_favorito)
            session.commit()
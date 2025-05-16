
from Infrastructure.Connection.CursosContext import dbcursos
from Domain.Entities.Aulas import Aulas

def create_aula(aula: Aulas):
    with dbcursos() as session:
        session.add(aula)
        session.commit()
        session.refresh(aula)  

def get_aula_by_id(aula_id: int) -> Aulas:
    with dbcursos() as session:
        return session.query(Aulas).filter(Aulas.AulaId == aula_id).first()

def get_all_aulas() -> list[Aulas]:
    with dbcursos() as session:
        return session.query(Aulas).all()

def update_aula(aula_id: int, aula: Aulas):
    with dbcursos() as session:
        aula_entity = session.query(Aulas).filter(Aulas.AulaId == aula_id).first()
        if aula_entity:
            aula_entity.Nome = aula.Nome
            aula_entity.Descricao = aula.Descricao
            aula_entity.Duracao = aula.Duracao
            aula_entity.Data_publicacao = aula.Data_publicacao
            session.commit()

def delete_aula(aula_id: int):
    with dbcursos() as session:
        aula_entity = session.query(Aulas).filter(Aulas.AulaId == aula_id).first()
        if aula_entity:
            session.delete(aula_entity)
            session.commit()

def close_aula():
    with dbcursos() as session:
        session.close()

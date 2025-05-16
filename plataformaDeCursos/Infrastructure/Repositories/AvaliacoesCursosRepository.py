from Domain.Entities.AvaliacoesCursos import avaliacoes_cursos
from Infrastructure.Connection.CursosContext import dbcursos
from Domain.Entities.AvaliacoesCursos import AvaliacaoEnum
from datetime import datetime

def add_avaliacao(curso_id: str, cpf: str, opiniao: str, avaliacao: AvaliacaoEnum):
    with dbcursos() as session:
        avaliacao_existente = session.query(avaliacoes_cursos).filter(avaliacoes_cursos.CursoId == curso_id, avaliacoes_cursos.Cpf == cpf).first()
        if avaliacao_existente:
            avaliacao_existente.Opniao = opiniao
            avaliacao_existente.Avaliacao = avaliacao
            avaliacao_existente.DataAvaliacao = datetime.today()
        else:
            nova_avaliacao = avaliacoes_cursos(
                CursoId=curso_id,
                Cpf=cpf,
                Opniao=opiniao,
                Avaliacao=avaliacao,
                DataAvaliacao=datetime.today())
            session.add(nova_avaliacao)
        session.commit()

def get_avaliacao(curso_id: str, cpf: str):
    with dbcursos() as session:
        return session.query(avaliacoes_cursos).filter(avaliacoes_cursos.CursoId == curso_id, avaliacoes_cursos.Cpf == cpf).first()

def get_all_avaliacoes(Cpf:str):
    with dbcursos() as session:
        return session.query(avaliacoes_cursos).filter(avaliacoes_cursos.Cpf == Cpf).all()

def update_avaliacao(curso_id: str, cpf: str, opiniao: str, avaliacao: AvaliacaoEnum):
    with dbcursos() as session:
        avaliacao_existente = session.query(avaliacoes_cursos).filter_by(CursoId=curso_id, Cpf=cpf).first()
        if avaliacao_existente:
            avaliacao_existente.Opniao = opiniao
            avaliacao_existente.Avaliacao = avaliacao
            session.commit()

def delete_avaliacao(curso_id: str, cpf: str):
    with dbcursos() as session:
        avaliacao = session.query(avaliacoes_cursos).filter(avaliacoes_cursos.CursoId == curso_id, avaliacoes_cursos.Cpf == cpf).first()
        if avaliacao:
            session.delete(avaliacao)
            session.commit()
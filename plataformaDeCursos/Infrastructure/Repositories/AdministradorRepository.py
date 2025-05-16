
from Infrastructure.Connection.CursosContext import dbcursos
from Domain.Entities.Administradores import administradores


def add_admin(administrador: administradores):
    with dbcursos() as session:
        session.add(administrador)
        session.commit()

def get_admin_by_id(cpf: str):
    with dbcursos() as session:
        return session.query(administradores).filter(administradores.Cpf == cpf).first()

def update_admin(cpf: str, administrador: administradores):
    with dbcursos() as session:
        admin_entity = session.query(administradores).filter(administradores.Cpf == cpf).first()
        if admin_entity:
            admin_entity.Cpf = administrador.Cpf
            admin_entity.Email = administrador.Email
            admin_entity.Nome = administrador.Nome
            admin_entity.Senha = administrador.Senha
            admin_entity.Banido = administrador.Banido
            session.commit()

def delete_admin(cpf: str):
    with dbcursos() as session:
        admin_entity = session.query(administradores).filter(administradores.Cpf == cpf).first()
        if admin_entity:
            session.delete(admin_entity)
            session.commit()

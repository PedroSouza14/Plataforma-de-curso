from Infrastructure.Connection.CursosContext import dbcursos
from Domain.Entities.Usuarios import Usuarios

def create_usuario(usuario:Usuarios):
    with dbcursos() as session:
        session.add(usuario) 
        session.commit()

def get_usuario_by_cpf(cpf:str)->Usuarios:
    with dbcursos() as session:
        return session.query(Usuarios).filter(Usuarios.Cpf==cpf).first()
    
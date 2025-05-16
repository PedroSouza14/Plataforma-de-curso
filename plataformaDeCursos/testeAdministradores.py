from Infrastructure.Repositories.AdministradorRepository import add_admin, get_admin_by_id, update_admin, delete_admin
from Infrastructure.Repositories.AdministradorRepository import administradores
from Infrastructure.Connection.CursosContext import dbcursos

cpf = "12345678922"

adm1 = get_admin_by_id(cpf)

if adm1 is not None:
    print(adm1.Cpf)
    print(adm1.Nome)
    print(adm1.Email)
    print(adm1.Senha)
    print(adm1.Banido)

    adm1.Nome = 'Novo Nome'
    adm1.Email = 'novoemail@example.com'
    adm1.Senha = 'novaSenha'
    adm1.Banido = False
    update_admin(cpf, adm1)
    print("Administrador atualizado")

else:
    adm2 = administradores()
    adm2.Cpf = cpf
    adm2.Email = 'duiwdnbiaowdia'
    adm2.Nome = 'Ameinda'
    adm2.Senha = '0777756'
    adm2.Banido = False
    print(adm2)

    add_admin(adm2)
    print("Administrador criado")

delete_admin(cpf)
print("Administrador excluído")
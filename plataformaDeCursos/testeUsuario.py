from Infrastructure.Repositories.UsuariosRepository import create_usuario, get_usuario_by_cpf
from Domain.Entities.Usuarios import Usuarios

cpf = "12345678901"

# Verifica se o usuario existe no banco
usuario2 = get_usuario_by_cpf(cpf)

# se o usuario existir, será exibido as informações dele
if usuario2 is not None:
    print (usuario2.Nome)
    print (usuario2.Email)
    print (usuario2.Senha)

# se o usuario não existir, ele será criado
else:
    usuario1 = Usuarios()
    usuario1.Cpf = cpf
    usuario1.Email = 'duiwdnbiaowdia'
    usuario1.Nome = 'Ameinda'
    usuario1.Senha = '0777756'
    usuario1.Banido = False
    print (usuario1)

    create_usuario(usuario1)

    print("Usuário criado")
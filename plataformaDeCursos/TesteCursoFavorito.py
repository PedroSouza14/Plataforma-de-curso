from Domain.Entities.CursosFavoritos import CursosFavoritos
from Infrastructure.Repositories.CursosFavoritosRepository import get_all_cursos_favoritados_by_cpf,Adicionar_cursos,remover_curso_favorito
from Infrastructure.Connection.CursosContext import dbcursos
from Infrastructure.Repositories.CursosFavoritosRepository import CursosFavoritos
cpf = "12345678901"
curso = 1234

cursos_favoritados = get_all_cursos_favoritados_by_cpf(cpf)

if cursos_favoritados:
    for curso_favorito in cursos_favoritados:
        print(curso_favorito.Cpf)
        print(curso_favorito.Curso)


else:
    curso2 = CursosFavoritos()
    curso2.Cpf = cpf
    curso2.Curso = curso
    print (curso2)

    Adicionar_cursos(curso2)

    print("Curso favoritado")

curso_id_to_remove = 1234
remover_curso_favorito(cpf, curso_id_to_remove)
print('Curso removido dos seus favoritos')
    
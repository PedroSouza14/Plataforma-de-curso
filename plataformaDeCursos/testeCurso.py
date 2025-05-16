from Infrastructure.Repositories.CursoRepository import get_all_cursos, create_cursos, update_cursos, delete_cursos
from Domain.Entities.Cursos import Cursos
if __name__ == "__main__":
    
    cursos = get_all_cursos()
    for curso in cursos:
        print(curso.Nome)

    novo_curso = Cursos(Nome="Novo Curso", Descricao="Descrição do novo curso")
    create_cursos(novo_curso)
    
    curso_id = 1
    curso_atualizado = Cursos(Nome="Curso Atualizado", Descricao="Descrição atualizada")
    update_cursos(curso_id, curso_atualizado)

    delete_cursos(curso_id)
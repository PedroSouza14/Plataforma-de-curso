
from Domain.Entities.AvaliacoesCursos import AvaliacaoEnum, avaliacoes_cursos
from Infrastructure.Connection.CursosContext import dbcursos
from Infrastructure.Repositories.AvaliacoesCursosRepository import add_avaliacao, get_all_avaliacoes, get_avaliacao, update_avaliacao, delete_avaliacao

def teste_avaliacao():
    curso_id = 'curso_123'
    cpf = '12345678901'
    opiniao = 'Ótimo curso, aprendi muito!'
    avaliacao = AvaliacaoEnum.muito_bom

     
    add_avaliacao(curso_id, cpf, opiniao, avaliacao)
    print("Avaliação adicionada")

    
    get_avaliacao(curso_id, cpf)
    

    
    nova_opiniao = 'Curso excelente!'
    nova_avaliacao = AvaliacaoEnum.bom
    update_avaliacao(curso_id, cpf, nova_opiniao, nova_avaliacao)
    print("Avaliação atualizada")

    
    todas_avaliacoes = get_all_avaliacoes(cpf)
    

    
    delete_avaliacao(curso_id, cpf)
    print("Avaliação excluída")

teste_avaliacao()
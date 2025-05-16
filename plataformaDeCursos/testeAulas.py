from Domain.Entities.Aulas import Aulas
from Infrastructure.Repositories.AulasRepository import create_aula, get_aula_by_id, get_all_aulas, update_aula, delete_aula

from datetime import datetime

def teste_aulas():
    
    nova_aula = Aulas(
        Nome="Introdução ao Python",
        Descricao="Uma aula introdutória sobre Python",
        Duracao=60,
        Data_publicacao=datetime.now()
    )
    create_aula(nova_aula)
    print("Aula criada")

    
    aula_id = nova_aula.AulaId
    aula_encontrada = get_aula_by_id(aula_id)
    if aula_encontrada:
        print(nova_aula)
    else:
        print("Aula não encontrada")

    
    aula_atualizada = Aulas(
        AulaId=aula_id,
        Nome="Introdução ao Python (Atualizado)",
        Descricao="Uma aula introdutória atualizada sobre Python",
        Duracao=75,
        Data_publicacao=datetime.now()
    )
    update_aula(aula_id, aula_atualizada)
    print("Aula atualizada")

    
    todas_aulas = get_all_aulas()
    print(f"Todas as aulas: {[aula.Nome for aula in todas_aulas]}")

    
    delete_aula(aula_id)
    print("Aula excluída")

    
    aula_excluida = get_aula_by_id(aula_id)
    if aula_excluida is None:
        print("Aula excluída com sucesso.")
    else:
        print("Falha ao excluir a aula.")


teste_aulas()

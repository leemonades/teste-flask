import pytest
from utils.verifica_dados import verifica_qtd_dados

def test_verifica_qtd_dados_com_preenchimento():
    """Teste para verificar se a função verifica_qtd_dados está preenchedo dados faltantes com
    a string "Sem dados"
    """
    alunos = ['Renato', 'Fernando', 'Rodrigo', 'Ana', 'Joana', 'Silvio', 'Carolina'] # 7 elementos
    notas = [15.00, 39.58, 62.92, 41.46, 48.33, 63.13] # 6 elementos

    df = verifica_qtd_dados(Alunos=alunos, Notas=notas)

    assert len(df) == 7
    assert df["Notas"].iloc[6] == "Sem dados"
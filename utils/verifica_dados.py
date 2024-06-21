import pandas as pd


def verifica_qtd_dados(**kwargs):
    """
    Verifica o tamanho máximo entre todas as listas fornecidas para garantir que a aplicação não quebre
    por falta de elemento

    Args:
        **kwargs: Nome da coluna e seu array de dados

    Returns:
        dataframe: DataFrame com todos os dados fornecidos e tratamento de dados faltantes
    """
    max_len = max(len(arg) for arg in kwargs.values())

    # preenche as listas com elementos faltantes com a string "Sem dados" para não quebrar a criação do dataframe
    for key, value in kwargs.items():
        if len(value) < max_len:
            kwargs[key] += (["Sem dados"] * (max_len - len(value)))

    # quando as listas de dados estiverem com o mesmo tamanho, gera o dataframe
    df = pd.DataFrame(kwargs)
    
    return df
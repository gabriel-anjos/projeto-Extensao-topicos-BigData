import pandas as pd

dados_vendas = {
    'Data': ['2023-08-01', '2023-08-01', '2023-08-02', '2023-08-02', '2023-08-03'],
    'Produto': ['Camiseta', 'Calça', 'Camiseta', 'Boné', 'Calça'],
    'Quantidade': [10, 5, 15, 20, 7],
    'Preco Unitario': [30, 80, 30, 25, 80]
}

df = pd.DataFrame(dados_vendas)
print(df)
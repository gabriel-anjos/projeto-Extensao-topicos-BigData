import pandas as pd

#               -----Uso da função DataFrame-----

# Simulando a leitura de um arquivo CSV com dados de vendas
dados_vendas = {
    'Data': ['2023-08-01', '2023-08-01', '2023-08-02', '2023-08-02', '2023-08-03'],
    'Produto': ['Camiseta', 'Calça', 'Camiseta', 'Boné', 'Calça'],
    'Quantidade': [10, 5, 15, 20, 7],
    'Preco Unitario': [30, 80, 30, 25, 80]
}

df = pd.DataFrame(dados_vendas)
print(df)

#               -----Conversão e Exploração dos Dados-----


# Ajustar o formato da coluna Data para o tipo datetime e adicionar uma coluna para a receita total (quantidade * preço unitário).

# Convertendo a coluna Data para o formato datetime
df['Data'] = pd.to_datetime(df['Data'])

# Criando uma nova coluna 'Receita' que é o resultado de Quantidade * Preco Unitario
df['Receita'] = df['Quantidade'] * df['Preco Unitario']

print(df)

#               -----Análise Agregada-----

#fazer uma análise por produto, para descobrir a quantidade total vendida e a receita total por produto.

# Agrupando por produto e calculando as estatísticas de quantidade e receita
vendas_por_produto = df.groupby('Produto').agg(
    Quantidade_Total=('Quantidade', 'sum'),
    Receita_Total=('Receita', 'sum')
).reset_index()

print(vendas_por_produto)

#Podemos também fazer uma análise por mês para saber a receita mensal.

# Extraindo o mês da coluna Data
df['Mes'] = df['Data'].dt.to_period('M')

# Agrupando por mês e somando a receita
vendas_por_mes = df.groupby('Mes').agg(
    Receita_Total=('Receita', 'sum'),
    Quantidade_Total=('Quantidade', 'sum')
).reset_index()

print(vendas_por_mes)

#               -----Exportando os Resultados-----


#Exportando esses dados para um arquivo CSV.
vendas_por_produto.to_csv('vendas_por_produto.csv', index=False)

# Exportando os dados agregados para um CSV
vendas_por_mes.to_csv('vendas_por_mes.csv', index=False)
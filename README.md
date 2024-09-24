# Projeto: Gestão de Vendas de uma Loja com Pandas

## Descrição
Este projeto utiliza a biblioteca `pandas` do Python para gerenciar e analisar os dados de vendas de uma loja fictícia. Ele abrange desde a importação dos dados até a geração de estatísticas de vendas por produto e por mês, com exportação dos resultados em formato CSV.

## Objetivos
- Carregar dados de vendas e manipular suas colunas.
- Analisar e agregar informações sobre quantidade de produtos vendidos e receita gerada.
- Exportar os resultados das análises para arquivos CSV.

## Estrutura dos Dados
Os dados de vendas simulados têm a seguinte estrutura:
- **Data**: Data da venda.
- **Produto**: Nome do produto vendido.
- **Quantidade**: Quantidade vendida.
- **Preço Unitário**: Preço unitário do produto.

## Passos do Projeto

1. **Importação e Carregamento dos Dados**: 
   - Leitura de um arquivo de vendas simulado usando `pandas.DataFrame`.
   - Exibição dos dados em formato de tabela.

2. **Manipulação e Limpeza dos Dados**:
   - Conversão da coluna de datas para o tipo `datetime`.
   - Criação de uma nova coluna chamada `Receita` (multiplicação da quantidade pelo preço unitário).

3. **Análise de Vendas**:
   - **Por Produto**: Agrupamento dos dados por produto, calculando a quantidade total vendida e a receita total.
   - **Por Mês**: Agrupamento das vendas por mês, somando a receita e a quantidade total de produtos vendidos.

4. **Exportação dos Resultados**:
   - Exportação dos dados agregados para arquivos CSV, contendo os resultados das análises por produto e por mês.

## Resultados Esperados


**Vendas por Produto**

| produtos | Quantidade_Total | Receita_Total |
|----------|------------------|---------------|
| Boné     | 20               | 500           |
| Calça    | 12               | 960           |
| Camiseta | 25               | 750           |


**Vendas por Mês**

| Mês     | Receita_total | Quantidade_Total |
|---------|---------------|------------------|
| 2024-08 | 2210          | 57               |

## Expansões Futuras

    Filtragem por produto ou período específico.
    Análise gráfica das vendas (ex.: gráficos de barras e linhas com matplotlib ou seaborn).
    Cálculo de estatísticas adicionais, como médias de vendas diárias ou mensais.
import pandas as pd

# Verificar quem bateu a meta, venda > que 55.000.

# Abrir os arquivos em Excel

# Para cada arquivo

# Verificar se algum valor na coluna de vendas dos arquivos, é maior que 55.000

# Se for maior que 55 mil

# Avisar o mês, o vendedor e o valor de venda


lista_meses = {'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho'}

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        Vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        Vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mes {mes} alguem bateu a meta. Vendedor:{Vendedor}, Vendas:{Vendas}')







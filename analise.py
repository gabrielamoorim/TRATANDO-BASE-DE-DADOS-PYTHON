
import pandas as pd
import os 
import plotly.express as px

lista_arquivo = os.listdir('vendas/')

tabela_total = pd.DataFrame()



for arquivo in lista_arquivo:
    if 'Vendas' in arquivo:
        tabela = pd.read_csv (f'vendas/{arquivo}')
        tabela_total = tabela_total._append(tabela)
        
print(tabela_total)

tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[['Quantidade Vendida']].sort_values(by='Quantidade Vendida', ascending= False)


tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']

tabela_faturamento = tabela_total.groupby('Produto').sum()


tabela_loja = tabela_total.groupby('Loja').sum()
tabela_loja = tabela_loja[['Faturamento']].sort_values(by='Faturamento', ascending= False)
print(tabela_loja)


grafico = px.bar(tabela_loja, x=tabela_loja.index, y='Faturamento')
grafico.show()

        
    
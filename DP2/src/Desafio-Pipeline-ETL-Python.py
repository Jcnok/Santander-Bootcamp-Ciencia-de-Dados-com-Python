#!/usr/bin/env python
# coding: utf-8

# # ETL e Análise de Gastos dos Deputados Federais
# ## Extração dos dados
# 

# A fonte de dados utilizada para este projeto é o portal de dados abertos da Câmara dos Deputados do Brasil, disponível no site [Dados Abertos](https://dadosabertos.camara.leg.br/swagger/api.html#api).
# <p>A coleta de dados será realizada por meio do uso da API disponibilizada pelo portal. </p>

# importação das bibliotecas
import pandas as pd
import requests

# Realizando o request dos dados dos deputados
url = "https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome"
resultado = requests.get(url)

# Convertendo em dataframe
deputados = pd.DataFrame(resultado.json()['dados'])

# Realizando o request dos gastos de 2023 dos deputatos 100 itens.
gastos = []
for id in deputados.id:
    url_despesa = "https://dadosabertos.camara.leg.br/api/v2/deputados/"
    url_despesa= url_despesa +str(id)+ "/despesas?ano=2023&itens=100&ordem=ASC&ordenarPor=ano"    
    resposta = requests.get(url_despesa)
    gasto = pd.DataFrame(resposta.json()['dados'])
    gasto['id'] = id
    gastos.append(gasto)       

# * **Para esse estudo vamos utilizar apenas os ['id', 'nome', 'siglaPartido','siglaUf','idLegislatura']**

deputados = deputados[['id', 'nome', 'siglaPartido','siglaUf','idLegislatura']]

# Concatenando 
total = pd.concat(gastos)

# Removendo os atributos que possuem valores ausentes para esse exemplo.
del total['dataDocumento']
del total['urlDocumento']
del total['numRessarcimento']

# Removendo linhas duplicadas se houver.
total.drop_duplicates()

from unidecode import unidecode
# Removendo todas as acentuações e os espaços duplos
total.nomeFornecedor = [unidecode(fornecedor).strip().upper() for fornecedor in total.nomeFornecedor]

# Removento tudo que LTDA e S.A e o que houver após também.
import re
exp_regurar = r"(LTDA|S\.A).*$" # "LTDA", "S.A" texto a ser removido
total.nomeFornecedor = [re.sub(exp_regurar,"",fornecedor).strip() for fornecedor in total.nomeFornecedor]

# realizando o merge de ambas as tabelas pelo atributo ID.
total = total.merge(deputados, on=['id'])
total.head()

# importando a lib
from sqlalchemy import create_engine

# Criando a conexão e o banco de dados gastos_deputados.db
engine = create_engine('sqlite:///database/gastos_deputados.db')

# Criando a tabela despesas_deputados com os dados ao banco de dados.
total.to_sql('despesas_deputados', engine, index=False)

# ## Análise EDA
total = pd.read_sql("select * from despesas_deputados;", engine)

total.value_counts('siglaPartido', ascending=True).plot(kind='barh');

# ### Os 10 deputados que mais tiveram despesas durante o período todo?
gastos_deputados = total.groupby(['nome']).sum()[['valorDocumento', 'valorLiquido']].reset_index()
gastos_deputados = gastos_deputados.sort_values('valorDocumento', ascending=False)
gastos_deputados.head(10)
gastos_deputados.head(10).sum()

# * **Os valores acumulados de despesas dos 10 deputados mais gastões no perído do Mês 2 ao final do Mês 9 chegaram na casa dos 3.900 milhão de Reais.**

# ### Os 10 Deputados que tiveram menos despesas durante todo o período?
gastos_deputados.tail(10)

# ### Quais os principais fornecedores?
total.nomeFornecedor.value_counts(ascending=False)[:10].plot(kind="barh");

# ### Quais os partidos que mais tiveram despesas?
gastos_partidos = total.groupby(['siglaPartido']).sum()[['valorDocumento']].reset_index()
gastos_partidos = gastos_partidos.sort_values('valorDocumento', ascending=False)
gastos_partidos.head()

# ### Qual a média das despesas por partido?
media_gastos_partidos = total.groupby(['siglaPartido']).mean()[['valorDocumento']].reset_index()
media_gastos_partidos = media_gastos_partidos.sort_values('valorDocumento', ascending=False)
media_gastos_partidos.head()

# ### Analisar os gastos mensais
gastos_partidos_mes = total.groupby(['mes'])['valorDocumento'].sum().reset_index()
gastos_partidos_mes = gastos_partidos_mes.sort_values(['mes'], ascending=True)
gastos_partidos_mes

# importação das libs.
import matplotlib.pyplot as plt
import seaborn as sns

# Função para criar um gráfico de barras
def plot_bar_chart(data, x, y, title, color='blue'):
    plt.figure(figsize=(10, 6))
    sns.barplot(data=data, x=x, y=y,color=color)
    plt.ticklabel_format(style='plain', axis='y')
    plt.title(title)
    plt.xticks(rotation=45)
    plt.show()

plot_bar_chart(gastos_partidos_mes,'mes', 'valorDocumento', 'Despesas totais por mês', color='#836FFF')
gastos_partidos_mes[:-1]['valorDocumento'].mean()


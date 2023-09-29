# ETL e Análise de Gastos dos Deputados Federais

<img src="./img/photo.jpg" >

## Objetivo

O objetivo deste projeto é extrair, transformar e carregar dados relacionados aos gastos dos deputados federais do Brasil. Em seguida, os dados serão analisados para identificar padrões de gastos do ano em exercicío.

<a name="ancora"></a>

# Índice

1. [Extração dos dados](#ancora1)
2. [Transformação](#ancora2)
3. [Carregamento(Load)](#ancora3)
4. [EDA](#ancora4)   
5. [Conclusão](#ancora5)   

<a name="ancora"></a>

<a id="ancora1"></a>

## Extração dos dados


A fonte de dados utilizada para este projeto é o portal de dados abertos da Câmara dos Deputados do Brasil, disponível no site [Dados Abertos](https://dadosabertos.camara.leg.br/swagger/api.html#api).
<p>A coleta de dados será realizada por meio do uso da API disponibilizada pelo portal. </p>


```python
# importação das bibliotecas
import pandas as pd
import requests
```


```python
# Realizando o request dos dados dos deputados
url = "https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome"
resultado = requests.get(url)
```


```python
# Convertendo em dataframe
deputados = pd.DataFrame(resultado.json()['dados'])
```


```python
deputados.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>uri</th>
      <th>nome</th>
      <th>siglaPartido</th>
      <th>uriPartido</th>
      <th>siglaUf</th>
      <th>idLegislatura</th>
      <th>urlFoto</th>
      <th>email</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>220593</td>
      <td>https://dadosabertos.camara.leg.br/api/v2/depu...</td>
      <td>Abilio Brunini</td>
      <td>PL</td>
      <td>https://dadosabertos.camara.leg.br/api/v2/part...</td>
      <td>MT</td>
      <td>57</td>
      <td>https://www.camara.leg.br/internet/deputado/ba...</td>
      <td>dep.abiliobrunini@camara.leg.br</td>
    </tr>
    <tr>
      <th>1</th>
      <td>204379</td>
      <td>https://dadosabertos.camara.leg.br/api/v2/depu...</td>
      <td>Acácio Favacho</td>
      <td>MDB</td>
      <td>https://dadosabertos.camara.leg.br/api/v2/part...</td>
      <td>AP</td>
      <td>57</td>
      <td>https://www.camara.leg.br/internet/deputado/ba...</td>
      <td>dep.acaciofavacho@camara.leg.br</td>
    </tr>
    <tr>
      <th>2</th>
      <td>220714</td>
      <td>https://dadosabertos.camara.leg.br/api/v2/depu...</td>
      <td>Adail Filho</td>
      <td>REPUBLICANOS</td>
      <td>https://dadosabertos.camara.leg.br/api/v2/part...</td>
      <td>AM</td>
      <td>57</td>
      <td>https://www.camara.leg.br/internet/deputado/ba...</td>
      <td>dep.adailfilho@camara.leg.br</td>
    </tr>
    <tr>
      <th>3</th>
      <td>221328</td>
      <td>https://dadosabertos.camara.leg.br/api/v2/depu...</td>
      <td>Adilson Barroso</td>
      <td>PL</td>
      <td>https://dadosabertos.camara.leg.br/api/v2/part...</td>
      <td>SP</td>
      <td>57</td>
      <td>https://www.camara.leg.br/internet/deputado/ba...</td>
      <td>dep.adilsonbarroso@camara.leg.br</td>
    </tr>
    <tr>
      <th>4</th>
      <td>204560</td>
      <td>https://dadosabertos.camara.leg.br/api/v2/depu...</td>
      <td>Adolfo Viana</td>
      <td>PSDB</td>
      <td>https://dadosabertos.camara.leg.br/api/v2/part...</td>
      <td>BA</td>
      <td>57</td>
      <td>https://www.camara.leg.br/internet/deputado/ba...</td>
      <td>dep.adolfoviana@camara.leg.br</td>
    </tr>
  </tbody>
</table>
</div>




```python
# conferindo o tamanho
deputados.shape
```




    (512, 9)



* **A variárvel 'deputados' é um dataframe que contém informações sobre os 513 deputados federais, cada linha representa um deputado e as colunas contêm diferentes atributos e informações sobre os mesmos.**

* **Certo agora já temos uma base de dados dos deputados, precisamos agora realizar o request dos gastos.**
* **Neste caso iremos realizar um request de 100 registros de cada id.**


```python
# Realizando o request dos gastos de 2023 dos deputatos 100 itens.
gastos = []
for id in deputados.id:
    url_despesa = "https://dadosabertos.camara.leg.br/api/v2/deputados/"
    url_despesa= url_despesa +str(id)+ "/despesas?ano=2023&itens=100&ordem=ASC&ordenarPor=ano"    
    resposta = requests.get(url_despesa)
    gasto = pd.DataFrame(resposta.json()['dados'])
    gasto['id'] = id
    gastos.append(gasto)       
```


```python
# Foram coletados 100 registros de cada deputado para esse exemplo.
len(gastos[510])
```




    100




```python
# 100 linhas e 18 colunas.
gastos[0].shape
```




    (100, 18)




```python
# visualizando os 5 ultimos registros do primeiro id.
gastos[0].tail()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ano</th>
      <th>mes</th>
      <th>tipoDespesa</th>
      <th>codDocumento</th>
      <th>tipoDocumento</th>
      <th>codTipoDocumento</th>
      <th>dataDocumento</th>
      <th>numDocumento</th>
      <th>valorDocumento</th>
      <th>urlDocumento</th>
      <th>nomeFornecedor</th>
      <th>cnpjCpfFornecedor</th>
      <th>valorLiquido</th>
      <th>valorGlosa</th>
      <th>numRessarcimento</th>
      <th>codLote</th>
      <th>parcela</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>95</th>
      <td>2023</td>
      <td>3</td>
      <td>COMBUSTÍVEIS E LUBRIFICANTES.</td>
      <td>7516348</td>
      <td>Nota Fiscal Eletrônica</td>
      <td>4</td>
      <td>2023-03-13</td>
      <td>5913</td>
      <td>192.38</td>
      <td>http://www.camara.leg.br/cota-parlamentar/nota...</td>
      <td>BOSQUE DA SAUDE COM. COMB. LTDA</td>
      <td>02823845000102</td>
      <td>192.38</td>
      <td>0.0</td>
      <td></td>
      <td>1918715</td>
      <td>0</td>
      <td>220593</td>
    </tr>
    <tr>
      <th>96</th>
      <td>2023</td>
      <td>3</td>
      <td>COMBUSTÍVEIS E LUBRIFICANTES.</td>
      <td>7516337</td>
      <td>Nota Fiscal Eletrônica</td>
      <td>4</td>
      <td>2023-03-25</td>
      <td>6050</td>
      <td>248.54</td>
      <td>http://www.camara.leg.br/cota-parlamentar/nota...</td>
      <td>BOSQUE DA SAUDE COM. COMB. LTDA</td>
      <td>02823845000102</td>
      <td>248.54</td>
      <td>0.0</td>
      <td></td>
      <td>1918714</td>
      <td>0</td>
      <td>220593</td>
    </tr>
    <tr>
      <th>97</th>
      <td>2023</td>
      <td>8</td>
      <td>COMBUSTÍVEIS E LUBRIFICANTES.</td>
      <td>7591454</td>
      <td>Nota Fiscal Eletrônica</td>
      <td>4</td>
      <td>2023-08-11</td>
      <td>659931</td>
      <td>30.90</td>
      <td>http://www.camara.leg.br/cota-parlamentar/nota...</td>
      <td>BURITI COM.DE DERIVADOS DE PET LTDA</td>
      <td>10827927000153</td>
      <td>30.90</td>
      <td>0.0</td>
      <td></td>
      <td>1959288</td>
      <td>0</td>
      <td>220593</td>
    </tr>
    <tr>
      <th>98</th>
      <td>2023</td>
      <td>4</td>
      <td>COMBUSTÍVEIS E LUBRIFICANTES.</td>
      <td>7553208</td>
      <td>Nota Fiscal</td>
      <td>0</td>
      <td>2023-04-17</td>
      <td>196407</td>
      <td>183.85</td>
      <td>https://www.camara.leg.br/cota-parlamentar/doc...</td>
      <td>CENTRO DE SERVS FRANGO ASSADO NORTE LT</td>
      <td>02896671001937</td>
      <td>183.85</td>
      <td>0.0</td>
      <td></td>
      <td>1938971</td>
      <td>0</td>
      <td>220593</td>
    </tr>
    <tr>
      <th>99</th>
      <td>2023</td>
      <td>8</td>
      <td>COMBUSTÍVEIS E LUBRIFICANTES.</td>
      <td>7602582</td>
      <td>Nota Fiscal Eletrônica</td>
      <td>4</td>
      <td>2023-08-19</td>
      <td>130045</td>
      <td>86.03</td>
      <td>http://www.camara.leg.br/cota-parlamentar/nota...</td>
      <td>COMERCIAL 364 DE COMBUSTIVEIS LTDA</td>
      <td>27744555000102</td>
      <td>86.03</td>
      <td>0.0</td>
      <td></td>
      <td>1965161</td>
      <td>0</td>
      <td>220593</td>
    </tr>
  </tbody>
</table>
</div>



[voltar](#ancora)

<a id="ancora2"></a>

## Transformação 


```python
# verificando os atributos
deputados.columns 
```




    Index(['id', 'uri', 'nome', 'siglaPartido', 'uriPartido', 'siglaUf',
           'idLegislatura', 'urlFoto', 'email'],
          dtype='object')



* **Para esse estudo vamos utilizar apenas os ['id', 'nome', 'siglaPartido','siglaUf','idLegislatura']**


```python
deputados = deputados[['id', 'nome', 'siglaPartido','siglaUf','idLegislatura']]
deputados.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>nome</th>
      <th>siglaPartido</th>
      <th>siglaUf</th>
      <th>idLegislatura</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>220593</td>
      <td>Abilio Brunini</td>
      <td>PL</td>
      <td>MT</td>
      <td>57</td>
    </tr>
    <tr>
      <th>1</th>
      <td>204379</td>
      <td>Acácio Favacho</td>
      <td>MDB</td>
      <td>AP</td>
      <td>57</td>
    </tr>
    <tr>
      <th>2</th>
      <td>220714</td>
      <td>Adail Filho</td>
      <td>REPUBLICANOS</td>
      <td>AM</td>
      <td>57</td>
    </tr>
    <tr>
      <th>3</th>
      <td>221328</td>
      <td>Adilson Barroso</td>
      <td>PL</td>
      <td>SP</td>
      <td>57</td>
    </tr>
    <tr>
      <th>4</th>
      <td>204560</td>
      <td>Adolfo Viana</td>
      <td>PSDB</td>
      <td>BA</td>
      <td>57</td>
    </tr>
  </tbody>
</table>
</div>



* **Vamos concatenar os 513 ids em um único dataframe usando o concat.**


```python
# Concatenando 
total = pd.concat(gastos)
```


```python
len(total)
```




    49023




```python
total.tail()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ano</th>
      <th>mes</th>
      <th>tipoDespesa</th>
      <th>codDocumento</th>
      <th>tipoDocumento</th>
      <th>codTipoDocumento</th>
      <th>dataDocumento</th>
      <th>numDocumento</th>
      <th>valorDocumento</th>
      <th>urlDocumento</th>
      <th>nomeFornecedor</th>
      <th>cnpjCpfFornecedor</th>
      <th>valorLiquido</th>
      <th>valorGlosa</th>
      <th>numRessarcimento</th>
      <th>codLote</th>
      <th>parcela</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>95</th>
      <td>2023.0</td>
      <td>8.0</td>
      <td>COMBUSTÍVEIS E LUBRIFICANTES.</td>
      <td>7601638.0</td>
      <td>Nota Fiscal Eletrônica</td>
      <td>4.0</td>
      <td>2023-08-29</td>
      <td>1332250</td>
      <td>250.00</td>
      <td>http://www.camara.leg.br/cota-parlamentar/nota...</td>
      <td>COMERCIAL DE COMBUSTIVEIS PLANETARIO LTDA.</td>
      <td>01157271000118</td>
      <td>250.00</td>
      <td>0.0</td>
      <td></td>
      <td>1964622.0</td>
      <td>0.0</td>
      <td>220552</td>
    </tr>
    <tr>
      <th>96</th>
      <td>2023.0</td>
      <td>3.0</td>
      <td>COMBUSTÍVEIS E LUBRIFICANTES.</td>
      <td>7513661.0</td>
      <td>Nota Fiscal Eletrônica</td>
      <td>4.0</td>
      <td>2023-03-11</td>
      <td>575375</td>
      <td>217.75</td>
      <td>http://www.camara.leg.br/cota-parlamentar/nota...</td>
      <td>COMERCIO DE COMBUSTIVEIS FLORESTAL LTDA</td>
      <td>02558109000921</td>
      <td>217.75</td>
      <td>0.0</td>
      <td></td>
      <td>1916796.0</td>
      <td>0.0</td>
      <td>220552</td>
    </tr>
    <tr>
      <th>97</th>
      <td>2023.0</td>
      <td>8.0</td>
      <td>COMBUSTÍVEIS E LUBRIFICANTES.</td>
      <td>7585426.0</td>
      <td>Nota Fiscal Eletrônica</td>
      <td>4.0</td>
      <td>2023-08-06</td>
      <td>2614301</td>
      <td>245.96</td>
      <td>http://www.camara.leg.br/cota-parlamentar/nota...</td>
      <td>COML BUFFON COMB E TRANSP LTDA - POSTO 26</td>
      <td>93489243002674</td>
      <td>226.06</td>
      <td>19.9</td>
      <td></td>
      <td>1956583.0</td>
      <td>0.0</td>
      <td>220552</td>
    </tr>
    <tr>
      <th>98</th>
      <td>2023.0</td>
      <td>7.0</td>
      <td>COMBUSTÍVEIS E LUBRIFICANTES.</td>
      <td>7585374.0</td>
      <td>Nota Fiscal Eletrônica</td>
      <td>4.0</td>
      <td>2023-07-12</td>
      <td>2220367</td>
      <td>251.52</td>
      <td>http://www.camara.leg.br/cota-parlamentar/nota...</td>
      <td>COML BUFFON COMB E TRANSP LTDA - POSTO 47</td>
      <td>93489243004707</td>
      <td>251.52</td>
      <td>0.0</td>
      <td></td>
      <td>1956581.0</td>
      <td>0.0</td>
      <td>220552</td>
    </tr>
    <tr>
      <th>99</th>
      <td>2023.0</td>
      <td>8.0</td>
      <td>COMBUSTÍVEIS E LUBRIFICANTES.</td>
      <td>7601513.0</td>
      <td>Nota Fiscal Eletrônica</td>
      <td>4.0</td>
      <td>2023-08-25</td>
      <td>2255317</td>
      <td>249.66</td>
      <td>http://www.camara.leg.br/cota-parlamentar/nota...</td>
      <td>COML BUFFON COMB E TRANSP LTDA - POSTO 47</td>
      <td>93489243004707</td>
      <td>249.66</td>
      <td>0.0</td>
      <td></td>
      <td>1964622.0</td>
      <td>0.0</td>
      <td>220552</td>
    </tr>
  </tbody>
</table>
</div>




```python
total.shape
```




    (49023, 18)




```python
# verificando valores ausentes
total.isnull().sum()
```




    ano                     0
    mes                     0
    tipoDespesa             0
    codDocumento            0
    tipoDocumento           0
    codTipoDocumento        0
    dataDocumento         270
    numDocumento            0
    valorDocumento          0
    urlDocumento         7803
    nomeFornecedor          0
    cnpjCpfFornecedor       0
    valorLiquido            0
    valorGlosa              0
    numRessarcimento        0
    codLote                 0
    parcela                 0
    id                      0
    dtype: int64




```python
# Removendo os atributos que possuem valores ausentes para esse exemplo.
del total['dataDocumento']
del total['urlDocumento']
```


```python
total.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ano</th>
      <th>mes</th>
      <th>tipoDespesa</th>
      <th>codDocumento</th>
      <th>tipoDocumento</th>
      <th>codTipoDocumento</th>
      <th>numDocumento</th>
      <th>valorDocumento</th>
      <th>nomeFornecedor</th>
      <th>cnpjCpfFornecedor</th>
      <th>valorLiquido</th>
      <th>valorGlosa</th>
      <th>numRessarcimento</th>
      <th>codLote</th>
      <th>parcela</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2023.0</td>
      <td>5.0</td>
      <td>MANUTENÇÃO DE ESCRITÓRIO DE APOIO À ATIVIDADE ...</td>
      <td>7552621.0</td>
      <td>Nota Fiscal</td>
      <td>0.0</td>
      <td>11533052023001</td>
      <td>43.2</td>
      <td>AGUAS CUIABA S.A</td>
      <td>14995581000153</td>
      <td>43.2</td>
      <td>0.0</td>
      <td></td>
      <td>1938600.0</td>
      <td>0.0</td>
      <td>220593</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2023.0</td>
      <td>6.0</td>
      <td>MANUTENÇÃO DE ESCRITÓRIO DE APOIO À ATIVIDADE ...</td>
      <td>7587236.0</td>
      <td>Recibos/Outros</td>
      <td>1.0</td>
      <td>11533062023001</td>
      <td>43.2</td>
      <td>AGUAS CUIABA S.A</td>
      <td>14995581000153</td>
      <td>43.2</td>
      <td>0.0</td>
      <td></td>
      <td>1957493.0</td>
      <td>0.0</td>
      <td>220593</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2023.0</td>
      <td>7.0</td>
      <td>MANUTENÇÃO DE ESCRITÓRIO DE APOIO À ATIVIDADE ...</td>
      <td>7587239.0</td>
      <td>Nota Fiscal</td>
      <td>0.0</td>
      <td>11533072023001</td>
      <td>43.2</td>
      <td>AGUAS CUIABA S.A</td>
      <td>14995581000153</td>
      <td>43.2</td>
      <td>0.0</td>
      <td></td>
      <td>1957494.0</td>
      <td>0.0</td>
      <td>220593</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2023.0</td>
      <td>8.0</td>
      <td>MANUTENÇÃO DE ESCRITÓRIO DE APOIO À ATIVIDADE ...</td>
      <td>7605225.0</td>
      <td>Nota Fiscal</td>
      <td>0.0</td>
      <td>11533082023001</td>
      <td>43.2</td>
      <td>AGUAS CUIABA S.A</td>
      <td>14995581000153</td>
      <td>43.2</td>
      <td>0.0</td>
      <td></td>
      <td>1966665.0</td>
      <td>0.0</td>
      <td>220593</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2023.0</td>
      <td>4.0</td>
      <td>MANUTENÇÃO DE ESCRITÓRIO DE APOIO À ATIVIDADE ...</td>
      <td>7538426.0</td>
      <td>Nota Fiscal</td>
      <td>0.0</td>
      <td>s/n</td>
      <td>43.2</td>
      <td>AGUAS CUIABA S.A</td>
      <td>14995581000153</td>
      <td>43.2</td>
      <td>0.0</td>
      <td></td>
      <td>1931086.0</td>
      <td>0.0</td>
      <td>220593</td>
    </tr>
  </tbody>
</table>
</div>




```python
# verificando a distribuição do atributo numRessarcimento
total.numRessarcimento.value_counts()
```




         42314
    0     6709
    Name: numRessarcimento, dtype: int64



* **nesse exemplo vamos remover o atributo 'numRessarcimento' também**.


```python
del total['numRessarcimento']
```


```python
total.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ano</th>
      <th>mes</th>
      <th>tipoDespesa</th>
      <th>codDocumento</th>
      <th>tipoDocumento</th>
      <th>codTipoDocumento</th>
      <th>numDocumento</th>
      <th>valorDocumento</th>
      <th>nomeFornecedor</th>
      <th>cnpjCpfFornecedor</th>
      <th>valorLiquido</th>
      <th>valorGlosa</th>
      <th>codLote</th>
      <th>parcela</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2023.0</td>
      <td>5.0</td>
      <td>MANUTENÇÃO DE ESCRITÓRIO DE APOIO À ATIVIDADE ...</td>
      <td>7552621.0</td>
      <td>Nota Fiscal</td>
      <td>0.0</td>
      <td>11533052023001</td>
      <td>43.2</td>
      <td>AGUAS CUIABA S.A</td>
      <td>14995581000153</td>
      <td>43.2</td>
      <td>0.0</td>
      <td>1938600.0</td>
      <td>0.0</td>
      <td>220593</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2023.0</td>
      <td>6.0</td>
      <td>MANUTENÇÃO DE ESCRITÓRIO DE APOIO À ATIVIDADE ...</td>
      <td>7587236.0</td>
      <td>Recibos/Outros</td>
      <td>1.0</td>
      <td>11533062023001</td>
      <td>43.2</td>
      <td>AGUAS CUIABA S.A</td>
      <td>14995581000153</td>
      <td>43.2</td>
      <td>0.0</td>
      <td>1957493.0</td>
      <td>0.0</td>
      <td>220593</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2023.0</td>
      <td>7.0</td>
      <td>MANUTENÇÃO DE ESCRITÓRIO DE APOIO À ATIVIDADE ...</td>
      <td>7587239.0</td>
      <td>Nota Fiscal</td>
      <td>0.0</td>
      <td>11533072023001</td>
      <td>43.2</td>
      <td>AGUAS CUIABA S.A</td>
      <td>14995581000153</td>
      <td>43.2</td>
      <td>0.0</td>
      <td>1957494.0</td>
      <td>0.0</td>
      <td>220593</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2023.0</td>
      <td>8.0</td>
      <td>MANUTENÇÃO DE ESCRITÓRIO DE APOIO À ATIVIDADE ...</td>
      <td>7605225.0</td>
      <td>Nota Fiscal</td>
      <td>0.0</td>
      <td>11533082023001</td>
      <td>43.2</td>
      <td>AGUAS CUIABA S.A</td>
      <td>14995581000153</td>
      <td>43.2</td>
      <td>0.0</td>
      <td>1966665.0</td>
      <td>0.0</td>
      <td>220593</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2023.0</td>
      <td>4.0</td>
      <td>MANUTENÇÃO DE ESCRITÓRIO DE APOIO À ATIVIDADE ...</td>
      <td>7538426.0</td>
      <td>Nota Fiscal</td>
      <td>0.0</td>
      <td>s/n</td>
      <td>43.2</td>
      <td>AGUAS CUIABA S.A</td>
      <td>14995581000153</td>
      <td>43.2</td>
      <td>0.0</td>
      <td>1931086.0</td>
      <td>0.0</td>
      <td>220593</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Removendo linhas duplicadas se houver.
print(total.shape)
total.drop_duplicates()
print(total.shape)
```

    (49023, 15)
    (49023, 15)
    


```python
total.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 49023 entries, 0 to 99
    Data columns (total 15 columns):
     #   Column             Non-Null Count  Dtype  
    ---  ------             --------------  -----  
     0   ano                49023 non-null  float64
     1   mes                49023 non-null  float64
     2   tipoDespesa        49023 non-null  object 
     3   codDocumento       49023 non-null  float64
     4   tipoDocumento      49023 non-null  object 
     5   codTipoDocumento   49023 non-null  float64
     6   numDocumento       49023 non-null  object 
     7   valorDocumento     49023 non-null  float64
     8   nomeFornecedor     49023 non-null  object 
     9   cnpjCpfFornecedor  49023 non-null  object 
     10  valorLiquido       49023 non-null  float64
     11  valorGlosa         49023 non-null  float64
     12  codLote            49023 non-null  float64
     13  parcela            49023 non-null  float64
     14  id                 49023 non-null  int64  
    dtypes: float64(9), int64(1), object(5)
    memory usage: 6.0+ MB
    


```python
total.describe()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ano</th>
      <th>mes</th>
      <th>codDocumento</th>
      <th>codTipoDocumento</th>
      <th>valorDocumento</th>
      <th>valorLiquido</th>
      <th>valorGlosa</th>
      <th>codLote</th>
      <th>parcela</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>49023.0</td>
      <td>49023.000000</td>
      <td>4.902300e+04</td>
      <td>49023.000000</td>
      <td>49023.000000</td>
      <td>49023.000000</td>
      <td>49023.000000</td>
      <td>4.902300e+04</td>
      <td>49023.000000</td>
      <td>49023.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>2023.0</td>
      <td>4.483120</td>
      <td>6.539757e+06</td>
      <td>1.790486</td>
      <td>1348.023479</td>
      <td>1341.657333</td>
      <td>6.317398</td>
      <td>1.670704e+06</td>
      <td>0.000041</td>
      <td>180450.891663</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.0</td>
      <td>2.432382</td>
      <td>2.533548e+06</td>
      <td>1.880205</td>
      <td>3338.725924</td>
      <td>3330.063181</td>
      <td>127.441130</td>
      <td>6.655180e+05</td>
      <td>0.006387</td>
      <td>49941.876047</td>
    </tr>
    <tr>
      <th>min</th>
      <td>2023.0</td>
      <td>1.000000</td>
      <td>0.000000e+00</td>
      <td>0.000000</td>
      <td>-1812.260000</td>
      <td>-1812.260000</td>
      <td>0.000000</td>
      <td>0.000000e+00</td>
      <td>0.000000</td>
      <td>62881.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2023.0</td>
      <td>2.000000</td>
      <td>7.500292e+06</td>
      <td>0.000000</td>
      <td>170.000000</td>
      <td>168.220000</td>
      <td>0.000000</td>
      <td>1.909818e+06</td>
      <td>0.000000</td>
      <td>160558.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>2023.0</td>
      <td>4.000000</td>
      <td>7.536204e+06</td>
      <td>1.000000</td>
      <td>270.050000</td>
      <td>269.250000</td>
      <td>0.000000</td>
      <td>1.929519e+06</td>
      <td>0.000000</td>
      <td>204456.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>2023.0</td>
      <td>6.000000</td>
      <td>7.573799e+06</td>
      <td>4.000000</td>
      <td>1144.740000</td>
      <td>1132.080000</td>
      <td>0.000000</td>
      <td>1.950428e+06</td>
      <td>0.000000</td>
      <td>220588.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>2023.0</td>
      <td>9.000000</td>
      <td>7.613905e+06</td>
      <td>4.000000</td>
      <td>124000.000000</td>
      <td>124000.000000</td>
      <td>14050.000000</td>
      <td>1.971259e+06</td>
      <td>1.000000</td>
      <td>226553.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Verificando a distribuição por fornecedores.
total.nomeFornecedor.value_counts().head(25)
```




    TAM                                                              3185
    GOL                                                              1385
    031 - 302 NORTE - CASCOL COMBUSTIVEIS PARA VEICULOS LTDA          950
    AZUL                                                              856
    AUTO POSTO CINCO ESTRELAS LTDA                                    678
    063 - 311 SUL - CASCOL COMBUSTIVEIS PARA VEICULOS LTDA            603
    UBER DO BRASIL TECNOLOGIA LTDA.                                   580
    WMS COMERCIO DE ARTIGOS DE PAPELARIA LTDA-ME                      536
    AUTO POSTO AEROPORTO LTDA                                         506
    AUTO POSTO 303 NORTE LTDA                                         488
    CELULAR FUNCIONAL                                                 457
    Telefônica Brasil S.A. VIVO                                       404
    AMORETTO CAFES EXPRESSO LTDA                                      324
    076 - MELHOR 10 - CASCOL COMBUSTIVEIS PARA VEICULOS LTDA          294
    RAMAL                                                             270
    CEMIG DISTRIBUIÇÃO S.A.                                           259
    POSTO DA TORRE EIRELI EPP                                         256
    Claro NXT Telecomunicações S.A                                    233
    AUTO POSTO CONCORDE LTDA                                          231
    DRA4 DERIVADOS DE PETROLEO LTDA                                   230
    CEEE - Companhia Estadual de Distribuição de Energia Elétrica     217
    COMPANHIA DE ELETRICIDADE DO ESTADO DA BAHIA                      213
    BRASAL COMBUSTIVEIS LTDA                                          201
    BELIZE COMPANY AUTO POSTO LTDA                                    172
    AUTO POSTO 302 SUL LTDA                                           167
    Name: nomeFornecedor, dtype: int64




```python
#Convertendo a coluna em uma lista para podermos realizar uma verificação mais detalhada
fornecedores = total.nomeFornecedor.value_counts().index.tolist()
```


```python
# Ordenando para comparar erros de digitação etc...
fornecedores.sort(reverse=True)
fornecedores[:10]
```




    ['ÍRIO JOSÉ FELIPE DIAS LTDA',
     'É RIO PRETO COMUNICAÇÃO E MARKETING DIGITAL EIRELE',
     'Águas de Joinville',
     'zeta  paineis ltda',
     'viviani silveira',
     'viu internet',
     'viewclinic ltda',
     'viação novo horizonte LTDA',
     'via Brasil MT-246 Concessionaria',
     'valdiney maciel da silva']



* **Existem alguns problemas aqui: erros de digitação, texto com letras minúsculas e maiúsculas misturadas, problemas de acentuação e casos em que "LTDA" e "S.A." foram acrescentados e casos em que não foram.**
* **Vamos remover todas as acentuações, e formatar tudo em letra maiúscula primeiro, depois os espaços e vamos remover tudo que contiver LTDA, S.A e depois dessas informações também para tentarmos corrigir a maior quantidade de informações incorretas.**


```python
from unidecode import unidecode
# Removendo todas as acentuações e os espaços duplos
total.nomeFornecedor = [unidecode(fornecedor).strip().upper() for fornecedor in total.nomeFornecedor]
```


```python
# Removento tudo que LTDA e S.A e o que houver após também.
import re
exp_regurar = r"(LTDA|S\.A).*$" # "LTDA", "S.A" texto a ser removido
total.nomeFornecedor = [re.sub(exp_regurar,"",fornecedor).strip() for fornecedor in total.nomeFornecedor]
```


```python
# Conferindo a distribuição.
total.nomeFornecedor.value_counts().head(25)
```




    TAM                                                              3185
    GOL                                                              1385
    031 - 302 NORTE - CASCOL COMBUSTIVEIS PARA VEICULOS               950
    AZUL                                                              856
    AUTO POSTO CINCO ESTRELAS                                         694
    063 - 311 SUL - CASCOL COMBUSTIVEIS PARA VEICULOS                 603
    UBER DO BRASIL TECNOLOGIA                                         582
    TELEFONICA BRASIL                                                 581
    WMS COMERCIO DE ARTIGOS DE PAPELARIA                              538
    AUTO POSTO AEROPORTO                                              506
    AUTO POSTO 303 NORTE                                              488
    CELULAR FUNCIONAL                                                 457
    CLARO NXT TELECOMUNICACOES                                        371
    AMORETTO CAFES EXPRESSO                                           324
    076 - MELHOR 10 - CASCOL COMBUSTIVEIS PARA VEICULOS               294
    RAMAL                                                             270
    CEMIG DISTRIBUICAO                                                259
    POSTO DA TORRE EIRELI EPP                                         256
    AUTO POSTO CONCORDE                                               231
    DRA4 DERIVADOS DE PETROLEO                                        230
    CEEE - COMPANHIA ESTADUAL DE DISTRIBUICAO DE ENERGIA ELETRICA     217
    COMPANHIA DE ELETRICIDADE DO ESTADO DA BAHIA                      213
    BRASAL COMBUSTIVEIS                                               201
    BELIZE COMPANY AUTO POSTO                                         172
    AUTO POSTO 302 SUL                                                167
    Name: nomeFornecedor, dtype: int64




```python
total.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ano</th>
      <th>mes</th>
      <th>tipoDespesa</th>
      <th>codDocumento</th>
      <th>tipoDocumento</th>
      <th>codTipoDocumento</th>
      <th>numDocumento</th>
      <th>valorDocumento</th>
      <th>nomeFornecedor</th>
      <th>cnpjCpfFornecedor</th>
      <th>valorLiquido</th>
      <th>valorGlosa</th>
      <th>codLote</th>
      <th>parcela</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2023.0</td>
      <td>5.0</td>
      <td>MANUTENÇÃO DE ESCRITÓRIO DE APOIO À ATIVIDADE ...</td>
      <td>7552621.0</td>
      <td>Nota Fiscal</td>
      <td>0.0</td>
      <td>11533052023001</td>
      <td>43.2</td>
      <td>AGUAS CUIABA</td>
      <td>14995581000153</td>
      <td>43.2</td>
      <td>0.0</td>
      <td>1938600.0</td>
      <td>0.0</td>
      <td>220593</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2023.0</td>
      <td>6.0</td>
      <td>MANUTENÇÃO DE ESCRITÓRIO DE APOIO À ATIVIDADE ...</td>
      <td>7587236.0</td>
      <td>Recibos/Outros</td>
      <td>1.0</td>
      <td>11533062023001</td>
      <td>43.2</td>
      <td>AGUAS CUIABA</td>
      <td>14995581000153</td>
      <td>43.2</td>
      <td>0.0</td>
      <td>1957493.0</td>
      <td>0.0</td>
      <td>220593</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2023.0</td>
      <td>7.0</td>
      <td>MANUTENÇÃO DE ESCRITÓRIO DE APOIO À ATIVIDADE ...</td>
      <td>7587239.0</td>
      <td>Nota Fiscal</td>
      <td>0.0</td>
      <td>11533072023001</td>
      <td>43.2</td>
      <td>AGUAS CUIABA</td>
      <td>14995581000153</td>
      <td>43.2</td>
      <td>0.0</td>
      <td>1957494.0</td>
      <td>0.0</td>
      <td>220593</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2023.0</td>
      <td>8.0</td>
      <td>MANUTENÇÃO DE ESCRITÓRIO DE APOIO À ATIVIDADE ...</td>
      <td>7605225.0</td>
      <td>Nota Fiscal</td>
      <td>0.0</td>
      <td>11533082023001</td>
      <td>43.2</td>
      <td>AGUAS CUIABA</td>
      <td>14995581000153</td>
      <td>43.2</td>
      <td>0.0</td>
      <td>1966665.0</td>
      <td>0.0</td>
      <td>220593</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2023.0</td>
      <td>4.0</td>
      <td>MANUTENÇÃO DE ESCRITÓRIO DE APOIO À ATIVIDADE ...</td>
      <td>7538426.0</td>
      <td>Nota Fiscal</td>
      <td>0.0</td>
      <td>s/n</td>
      <td>43.2</td>
      <td>AGUAS CUIABA</td>
      <td>14995581000153</td>
      <td>43.2</td>
      <td>0.0</td>
      <td>1931086.0</td>
      <td>0.0</td>
      <td>220593</td>
    </tr>
  </tbody>
</table>
</div>



* **Bom agora que já temos as tabelas deputados e gastos vamos realizar o merge em uma única tabela para depois realizarmos a etape de Load.**


```python
# realizando o merge de ambas as tabelas pelo atributo ID.
total = total.merge(deputados, on=['id'])
total.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ano</th>
      <th>mes</th>
      <th>tipoDespesa</th>
      <th>codDocumento</th>
      <th>tipoDocumento</th>
      <th>codTipoDocumento</th>
      <th>numDocumento</th>
      <th>valorDocumento</th>
      <th>nomeFornecedor</th>
      <th>cnpjCpfFornecedor</th>
      <th>valorLiquido</th>
      <th>valorGlosa</th>
      <th>codLote</th>
      <th>parcela</th>
      <th>id</th>
      <th>nome</th>
      <th>siglaPartido</th>
      <th>siglaUf</th>
      <th>idLegislatura</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2023.0</td>
      <td>5.0</td>
      <td>MANUTENÇÃO DE ESCRITÓRIO DE APOIO À ATIVIDADE ...</td>
      <td>7552621.0</td>
      <td>Nota Fiscal</td>
      <td>0.0</td>
      <td>11533052023001</td>
      <td>43.2</td>
      <td>AGUAS CUIABA</td>
      <td>14995581000153</td>
      <td>43.2</td>
      <td>0.0</td>
      <td>1938600.0</td>
      <td>0.0</td>
      <td>220593</td>
      <td>Abilio Brunini</td>
      <td>PL</td>
      <td>MT</td>
      <td>57</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2023.0</td>
      <td>6.0</td>
      <td>MANUTENÇÃO DE ESCRITÓRIO DE APOIO À ATIVIDADE ...</td>
      <td>7587236.0</td>
      <td>Recibos/Outros</td>
      <td>1.0</td>
      <td>11533062023001</td>
      <td>43.2</td>
      <td>AGUAS CUIABA</td>
      <td>14995581000153</td>
      <td>43.2</td>
      <td>0.0</td>
      <td>1957493.0</td>
      <td>0.0</td>
      <td>220593</td>
      <td>Abilio Brunini</td>
      <td>PL</td>
      <td>MT</td>
      <td>57</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2023.0</td>
      <td>7.0</td>
      <td>MANUTENÇÃO DE ESCRITÓRIO DE APOIO À ATIVIDADE ...</td>
      <td>7587239.0</td>
      <td>Nota Fiscal</td>
      <td>0.0</td>
      <td>11533072023001</td>
      <td>43.2</td>
      <td>AGUAS CUIABA</td>
      <td>14995581000153</td>
      <td>43.2</td>
      <td>0.0</td>
      <td>1957494.0</td>
      <td>0.0</td>
      <td>220593</td>
      <td>Abilio Brunini</td>
      <td>PL</td>
      <td>MT</td>
      <td>57</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2023.0</td>
      <td>8.0</td>
      <td>MANUTENÇÃO DE ESCRITÓRIO DE APOIO À ATIVIDADE ...</td>
      <td>7605225.0</td>
      <td>Nota Fiscal</td>
      <td>0.0</td>
      <td>11533082023001</td>
      <td>43.2</td>
      <td>AGUAS CUIABA</td>
      <td>14995581000153</td>
      <td>43.2</td>
      <td>0.0</td>
      <td>1966665.0</td>
      <td>0.0</td>
      <td>220593</td>
      <td>Abilio Brunini</td>
      <td>PL</td>
      <td>MT</td>
      <td>57</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2023.0</td>
      <td>4.0</td>
      <td>MANUTENÇÃO DE ESCRITÓRIO DE APOIO À ATIVIDADE ...</td>
      <td>7538426.0</td>
      <td>Nota Fiscal</td>
      <td>0.0</td>
      <td>s/n</td>
      <td>43.2</td>
      <td>AGUAS CUIABA</td>
      <td>14995581000153</td>
      <td>43.2</td>
      <td>0.0</td>
      <td>1931086.0</td>
      <td>0.0</td>
      <td>220593</td>
      <td>Abilio Brunini</td>
      <td>PL</td>
      <td>MT</td>
      <td>57</td>
    </tr>
  </tbody>
</table>
</div>



* **Bom com isso terminamos nossa etapa de transformação, claro que poderíamos tratar mais dados e fazer uma verificação mais detalhada, porém nesse momento vamos parar por aqui, agora precisamos partir para próxima etapa que é a de carregamento.**
* **Para o carregamento vamos usar um banco de dados relacional sqLite, pois são poucos dados o que se encaixa perfeitamente nesse caso.**

[voltar](#ancora)

<a id="ancora3"></a>

## Carregamento(Load)


```python
# importando a lib
from sqlalchemy import create_engine
```


```python
# Criando a conexão e o banco de dados gastos_deputados.db
engine = create_engine('sqlite:///database/gastos_deputados.db')
```


```python
# Criando a tabela despesas_deputados com os dados ao banco de dados.
total.to_sql('despesas_deputados', engine, index=False)
```




    49023



* **Pronto com isso concluímos todas as etapas do ETL**.
* **Agora podemos carregar os dados salvos e partir para uma analise exploratória.**

[voltar](#ancora)

<a id="ancora4"></a>

## Análise EDA


```python
total = pd.read_sql("select * from despesas_deputados;", engine)
```


```python
total.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ano</th>
      <th>mes</th>
      <th>tipoDespesa</th>
      <th>codDocumento</th>
      <th>tipoDocumento</th>
      <th>codTipoDocumento</th>
      <th>numDocumento</th>
      <th>valorDocumento</th>
      <th>nomeFornecedor</th>
      <th>cnpjCpfFornecedor</th>
      <th>valorLiquido</th>
      <th>valorGlosa</th>
      <th>codLote</th>
      <th>parcela</th>
      <th>id</th>
      <th>nome</th>
      <th>siglaPartido</th>
      <th>siglaUf</th>
      <th>idLegislatura</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2023.0</td>
      <td>5.0</td>
      <td>MANUTENÇÃO DE ESCRITÓRIO DE APOIO À ATIVIDADE ...</td>
      <td>7552621.0</td>
      <td>Nota Fiscal</td>
      <td>0.0</td>
      <td>11533052023001</td>
      <td>43.2</td>
      <td>AGUAS CUIABA</td>
      <td>14995581000153</td>
      <td>43.2</td>
      <td>0.0</td>
      <td>1938600.0</td>
      <td>0.0</td>
      <td>220593</td>
      <td>Abilio Brunini</td>
      <td>PL</td>
      <td>MT</td>
      <td>57</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2023.0</td>
      <td>6.0</td>
      <td>MANUTENÇÃO DE ESCRITÓRIO DE APOIO À ATIVIDADE ...</td>
      <td>7587236.0</td>
      <td>Recibos/Outros</td>
      <td>1.0</td>
      <td>11533062023001</td>
      <td>43.2</td>
      <td>AGUAS CUIABA</td>
      <td>14995581000153</td>
      <td>43.2</td>
      <td>0.0</td>
      <td>1957493.0</td>
      <td>0.0</td>
      <td>220593</td>
      <td>Abilio Brunini</td>
      <td>PL</td>
      <td>MT</td>
      <td>57</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2023.0</td>
      <td>7.0</td>
      <td>MANUTENÇÃO DE ESCRITÓRIO DE APOIO À ATIVIDADE ...</td>
      <td>7587239.0</td>
      <td>Nota Fiscal</td>
      <td>0.0</td>
      <td>11533072023001</td>
      <td>43.2</td>
      <td>AGUAS CUIABA</td>
      <td>14995581000153</td>
      <td>43.2</td>
      <td>0.0</td>
      <td>1957494.0</td>
      <td>0.0</td>
      <td>220593</td>
      <td>Abilio Brunini</td>
      <td>PL</td>
      <td>MT</td>
      <td>57</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2023.0</td>
      <td>8.0</td>
      <td>MANUTENÇÃO DE ESCRITÓRIO DE APOIO À ATIVIDADE ...</td>
      <td>7605225.0</td>
      <td>Nota Fiscal</td>
      <td>0.0</td>
      <td>11533082023001</td>
      <td>43.2</td>
      <td>AGUAS CUIABA</td>
      <td>14995581000153</td>
      <td>43.2</td>
      <td>0.0</td>
      <td>1966665.0</td>
      <td>0.0</td>
      <td>220593</td>
      <td>Abilio Brunini</td>
      <td>PL</td>
      <td>MT</td>
      <td>57</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2023.0</td>
      <td>4.0</td>
      <td>MANUTENÇÃO DE ESCRITÓRIO DE APOIO À ATIVIDADE ...</td>
      <td>7538426.0</td>
      <td>Nota Fiscal</td>
      <td>0.0</td>
      <td>s/n</td>
      <td>43.2</td>
      <td>AGUAS CUIABA</td>
      <td>14995581000153</td>
      <td>43.2</td>
      <td>0.0</td>
      <td>1931086.0</td>
      <td>0.0</td>
      <td>220593</td>
      <td>Abilio Brunini</td>
      <td>PL</td>
      <td>MT</td>
      <td>57</td>
    </tr>
  </tbody>
</table>
</div>



### Qual a distribuição por partidos?


```python
total.value_counts('siglaPartido', ascending=True).plot(kind='barh');
```


    
![png](./img/output_60_0.png)
    


### Os 10 deputados que mais tiveram despesas durante o período todo?


```python
gastos_deputados = total.groupby(['nome']).sum()[['valorDocumento', 'valorLiquido']].reset_index()
gastos_deputados = gastos_deputados.sort_values('valorDocumento', ascending=False)
gastos_deputados.head(10)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>nome</th>
      <th>valorDocumento</th>
      <th>valorLiquido</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>334</th>
      <td>Marcos Aurélio Sampaio</td>
      <td>408771.46</td>
      <td>408769.90</td>
    </tr>
    <tr>
      <th>491</th>
      <td>Vinicius Gurgel</td>
      <td>398189.31</td>
      <td>398189.31</td>
    </tr>
    <tr>
      <th>453</th>
      <td>Rubens Pereira Júnior</td>
      <td>397659.14</td>
      <td>397659.14</td>
    </tr>
    <tr>
      <th>141</th>
      <td>Dilvanda Faro</td>
      <td>395749.85</td>
      <td>387140.52</td>
    </tr>
    <tr>
      <th>509</th>
      <td>Átila Lins</td>
      <td>395358.49</td>
      <td>395211.78</td>
    </tr>
    <tr>
      <th>144</th>
      <td>Domingos Neto</td>
      <td>390552.16</td>
      <td>389829.21</td>
    </tr>
    <tr>
      <th>134</th>
      <td>Delegado Éder Mauro</td>
      <td>387706.58</td>
      <td>387706.58</td>
    </tr>
    <tr>
      <th>92</th>
      <td>Cleber Verde</td>
      <td>385865.57</td>
      <td>385865.57</td>
    </tr>
    <tr>
      <th>489</th>
      <td>Vicentinho Júnior</td>
      <td>378002.37</td>
      <td>378002.37</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Acácio Favacho</td>
      <td>377485.95</td>
      <td>377485.07</td>
    </tr>
  </tbody>
</table>
</div>




```python
gastos_deputados.head(10).sum()
```




    nome              Marcos Aurélio SampaioVinicius GurgelRubens Pe...
    valorDocumento                                           3915340.88
    valorLiquido                                             3905859.45
    dtype: object



* **Os valores acumulados de despesas dos 10 deputados mais gastões no perído do Mês 2 ao final do Mês 9 chegaram na casa dos 3.900 milhão de Reais.**

### Os 10 Deputados que tiveram menos despesas durante todo o período?


```python
gastos_deputados.tail(10)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>nome</th>
      <th>valorDocumento</th>
      <th>valorLiquido</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>325</th>
      <td>Marcelo Calero</td>
      <td>22421.68</td>
      <td>22321.07</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Adail Filho</td>
      <td>21856.35</td>
      <td>21856.35</td>
    </tr>
    <tr>
      <th>318</th>
      <td>Lula da Fonte</td>
      <td>20652.92</td>
      <td>20408.13</td>
    </tr>
    <tr>
      <th>365</th>
      <td>Márcio Correa</td>
      <td>20000.00</td>
      <td>20000.00</td>
    </tr>
    <tr>
      <th>186</th>
      <td>Fernanda Pessoa</td>
      <td>19168.05</td>
      <td>19143.06</td>
    </tr>
    <tr>
      <th>349</th>
      <td>Mauricio do Vôlei</td>
      <td>18819.73</td>
      <td>18819.73</td>
    </tr>
    <tr>
      <th>274</th>
      <td>Juliana Cardoso</td>
      <td>18725.47</td>
      <td>18725.47</td>
    </tr>
    <tr>
      <th>414</th>
      <td>Priscila Costa</td>
      <td>15806.95</td>
      <td>15806.95</td>
    </tr>
    <tr>
      <th>147</th>
      <td>Doutor Luizinho</td>
      <td>15260.33</td>
      <td>15260.33</td>
    </tr>
    <tr>
      <th>117</th>
      <td>Daniela do Waguinho</td>
      <td>13275.95</td>
      <td>13267.87</td>
    </tr>
  </tbody>
</table>
</div>



### Quais os principais fornecedores?


```python
total.nomeFornecedor.value_counts(ascending=False)[:10].plot(kind="barh");
```


    
![png](./img/output_68_0.png)
    


* **Aparentemente as maiores despesas provém de companhias aéreas.**
* **A vida não deve estar fácil para esses deputados, pegando transporte público em horário de pico.**

### Quais os partidos que mais tiveram despesas?


```python
gastos_partidos = total.groupby(['siglaPartido']).sum()[['valorDocumento']].reset_index()
gastos_partidos = gastos_partidos.sort_values('valorDocumento', ascending=False)
gastos_partidos.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>siglaPartido</th>
      <th>valorDocumento</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>PL</td>
      <td>13184802.76</td>
    </tr>
    <tr>
      <th>14</th>
      <td>PT</td>
      <td>8293306.06</td>
    </tr>
    <tr>
      <th>19</th>
      <td>UNIÃO</td>
      <td>7828435.36</td>
    </tr>
    <tr>
      <th>9</th>
      <td>PP</td>
      <td>6373352.30</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MDB</td>
      <td>5647371.69</td>
    </tr>
  </tbody>
</table>
</div>



* **Acima estão o 5 partidos que tiveram mais despesas, porém essa não é a melhor forma de confirmação, pois a disdrituição dos deputados não seguem uma proporção equilibrada. Para esse cenário podemos utilizar a média de gastos por partido.**

### Qual a média das despesas por partido?


```python
media_gastos_partidos = total.groupby(['siglaPartido']).mean()[['valorDocumento']].reset_index()
media_gastos_partidos = media_gastos_partidos.sort_values('valorDocumento', ascending=False)
media_gastos_partidos.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>siglaPartido</th>
      <th>valorDocumento</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8</th>
      <td>PODE</td>
      <td>1772.380275</td>
    </tr>
    <tr>
      <th>5</th>
      <td>PCdoB</td>
      <td>1529.912014</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MDB</td>
      <td>1474.894670</td>
    </tr>
    <tr>
      <th>17</th>
      <td>REPUBLICANOS</td>
      <td>1451.951481</td>
    </tr>
    <tr>
      <th>7</th>
      <td>PL</td>
      <td>1400.403904</td>
    </tr>
  </tbody>
</table>
</div>



* **Acima podemos ter uma visão real que qual partido estão gastando mais, através das médias das despesas.**

### Analisar os gastos mensais


```python
gastos_partidos_mes = total.groupby(['mes'])['valorDocumento'].sum().reset_index()
gastos_partidos_mes = gastos_partidos_mes.sort_values(['mes'], ascending=True)
gastos_partidos_mes
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>mes</th>
      <th>valorDocumento</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>8837847.84</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.0</td>
      <td>6501967.04</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.0</td>
      <td>8077845.34</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.0</td>
      <td>8194895.77</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>8967956.38</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6.0</td>
      <td>8066411.80</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7.0</td>
      <td>7901487.05</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8.0</td>
      <td>7611575.48</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9.0</td>
      <td>1924168.31</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```


```python
plot_bar_chart(gastos_partidos_mes,'mes', 'valorDocumento', 'Despesas totais por mês', color='#836FFF')
```


    
![png](./img/output_79_0.png)
    



```python
gastos_partidos_mes[:-1]['valorDocumento'].mean()
```




    8019998.3374999985



* **Aparentemente existe um padrão na casa de 8 milhão por mês.**

[voltar](#ancora)

<a id="ancora5"></a>

## Conclusão

**Com isso concluí todas as etapas da ETL. Extraí os dados dos deputados federeais e suas despesas via API dos Dados Abertos, realizei a limpeza, correção de erros e o merge das tabelas na etapa de transformação e por fim salvei a tabelas no banco de dados SQLite finalizando a etapa de Carregamento.**
**Com os dados já preparados, fiz extração do banco de dados para uma breve análise exploratória, para responder algumas questões sobre a distribuição dos partidos, as principais despesas e fornecedores, a média das despesas por partido e rank dos 10 deputados com maior e menor despesas.**

[voltar](#ancora)


```python

```

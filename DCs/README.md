# Resolução dos desafios de Código Python.

<img src="./img/python.jpg" referrerpolicy="same-origin" style="display: block; object-fit: cover; border-radius: 0px; width: 100%; height: 30vh; opacity: 1; object-position: center 50%;">

<a name="ancora"></a>

# Desafios:

1. [Equilibrando Saldo](#ancora1)
2. [Organizando seus Ativos](#ancora2)
3. [Condicionalmente Rico](#ancora3)
4. [Juros Compostos](#ancora4)   
5. [O Grande Depósito](#ancora5)  

<a name="ancora"></a>

<a id="ancora1"></a>
## Desafio: Equilibrando Saldo

### Descrição
Para esse desafio, considere que você foi contratado por uma empresa bancária para auxiliar nas implementações e melhorias do sistema empresarial. Em uma análise inicial, foi identificado pela equipe financeira a necessidade de desenvolver uma solução que permita ao cliente equilibrar seu saldo bancário. Dessa forma, o programa deve solicitar uma entrada que representa o saldo atual do funcionário, e após, seja informado o valor de duas transações, sendo elas: um depósito e um saque. O programa deve atualizar o saldo com base nas transações e exibir o saldo final.

Informação: As transações de depósito e retirada devem ser tratadas como valores positivos e negativos, respectivamente, para garantir que o cálculo do saldo final seja realizado corretamente.
 

### Entrada
* saldo_atual: um número decimal representando o saldo atual da conta bancária.
* valor_deposito: um número decimal representando o valor a ser depositado na conta.
* valor_retirada: um número decimal representando o valor a ser retirado da conta.
* Regra de Formatação: Considere apenas uma casa decimal para esse desafio.

### Saída
 Um número decimal que representa o saldo atualizado na conta bancária após o processamento das transações.


### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Exemplo de Entrada | Exemplo de Saída
:-----------------:|:------------------:
1000  |
500   | Saldo atualizado na conta: 1300.0
200   |
----- | ---------------------------------
100   |
10    | Saldo atualizado na conta: 60.0
50    |
----- | ---------------------------------
5000  | 
500   | Saldo atualizado na conta: 5300.0
200   |


```python
#TODO: Calcular o saldo atualizado de acordo com a descrição deste desafio.
def calcular_saldo():
  saldo_atual = float(input())
  valor_deposito = float(input())
  valor_retirada = float(input())  
  saldo_atual += valor_deposito - valor_retirada 
  #TODO: Imprimir o a saída de conforme a tabela de exemplos (uma casa decimal).
  print(f"Saldo atualizado na conta: {saldo_atual:.1f}")
# executa a função
calcular_saldo()
```

    1000
    500
    200
    Saldo atualizado na conta: 1300.0
    

[voltar](#ancora)

<a id="ancora2"></a>
## Desafio: Organizando seus Ativos

### Descrição
Após uma análise cuidadosa realizada pela equipe de desenvolvimento de uma empresa bancaria, foi identificado a necessidade de uma nova funcionalidade para otimizar os processos e melhorias da experiência dos usuários. Agora, sua tarefa é implementar uma solução que organize em ordem alfabética uma lista de ativos que será informada pelos usuários. Os ativos são representados por strings que representam seus tipos, como por exemplo: Reservas de liquidez, Ativos intangiveis e dentre outros.

### Entrada
A primeira entrada consiste em um número inteiro que representa a  quantidade de ativos que o usuário possui. Em seguida, o usuário deverá  informar, em linhas separadas, os tipos (strings) dos respectivos ativos.

### Saída
Seu programa deve exibir a lista de Ativos organizada em ordem alfabética. Cada ativo deve ser apresentado em uma linha separada.

### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Exemplo de Entrada | Exemplo de Saída
:-----------------:|:------------------:
3                         | Deposito
Financiamento de Imovel   | Financiamento de Imovel
Deposito                  | Reservas Bancarias
Reservas Bancarias        |
----- | ---------------------------------
3                         | Carteiras de credito 
Carteiras de credito      | Derivativos financeiros
Investimentos em titulos  | Investimentos em titulos
Derivativos financeiros   |
----- | ---------------------------------
3                         | Ativos intangiveis 
Reservas de liquidez      | Fundos de investimento
Ativos intangiveis        | Reservas de liquidez
Fundos de investimento    |


```python
ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input())

# Entrada dos códigos dos ativos
for _ in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)
# TODO: Ordenar os ativos em ordem alfabética.
ativos.sort()
# TODO: Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.
for i in ativos:
    print(i)
```

    3
    julio
    cesar
    okuda
    cesar
    julio
    okuda
    

[voltar](#ancora)

<a id="ancora3"></a>
## Desafio: Condicionalmente Rico

### Descrição
Uma nova feature para um sistema bancário foi analisada pela equipe de desenvolvimento e será uma das tarefas a serem trabalhadas durante a sprint, como desenvolvedor da empresa você recebeu os requisitos para a nova implementação que consiste em uma solução algorítmica que permita aos clientes realizarem saques em caixas eletrônicos. No entanto, existem algumas regras a serem seguidas para garantir que um saque possa ser realizado com sucesso.

### Regras do saque:

- Cada cliente digitará o valor do seu saldoTotal de sua conta bancária e o valorSaque.
- Um saque só pode ser realizado se o saldoDisponível na conta for igual ou superior ao valor solicitado.
- Se o saldo for suficiente, o valor solicitado deve ser subtraído do saldo disponível, indicando que o saque foi realizado.
- Se o saldo for insuficiente, o saque não deve ser realizado e uma mensagem adequada deve ser exibida.

### Entrada
- A entrada consiste em dois valores inteiros que representam o total do saldo da conta e o valor do saque.

### Saída
- Se o saque for realizado com sucesso, exibir a mensagem "Saque realizado com sucesso! Novo saldo: {saldo}", onde {saldo} é o novo saldo disponível na conta.

- Se o saque não for possível devido a saldo insuficiente, exibir a mensagem "Saldo insuficiente. Saque nao realizado!"

### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Exemplo de Entrada | Exemplo de Saída
:-----------------:|:------------------:
1000  | Saque realizado com sucesso! Novo saldo: 800
200   | 
----- | ---------------------------------
1500  | Saldo insuficiente. Saque nao realizado!
1800  | 
----- | ---------------------------------
300   | Saque realizado com sucesso. Novo saldo: 100
200   |


```python
# Entrada de dados
saldo_total = int(input())
valor_saque = int(input())

# TODO: Criar as condições necessárias para impressão da saída, vide tabela de exemplos.
if saldo_total >= valor_saque:
    saldo = saldo_total - valor_saque
    print(f"Saque realizado com sucesso. Novo saldo: {saldo}")
else:
    print("Saldo insuficiente. Saque nao realizado!")
```

    1000
    200
    Saque realizado com sucesso! Novo saldo: 800
    

[voltar](#ancora)

<a id="ancora4"></a>
## Desafio: Juros Compostos

### Desafio
Imagine que você está desenvolvendo um aplicativo para um banco que deseja calcular os juros compostos de um investimento. Seu objetivo é criar uma função que receba três parâmetros: o valor inicial do investimento, a taxa de juros anual e o período de tempo em anos. A função deve calcular e retornar o valor final do investimento após o período determinado, levando em consideração os juros compostos.

### Entrada:
- A função deve receber os seguintes parâmetros:

    - valor_inicial: um número inteiro ou decimal representando o valor inicial do investimento.

    - taxa_juros: um número decimal representando a taxa de juros anual. Por exemplo, se a taxa for de 5%, o valor passado será 0.05.

    - periodo: um número inteiro representando a quantidade de anos do investimento.

### Saída:
- A função deve retornar o valor final do investimento após o período determinado, considerando os juros compostos. O valor final deve ser arredondado para duas casas decimais.

### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Exemplo de Entrada | Exemplo de Saída
:-----------------:|:------------------:
5000   |
0.08   | Valor final do investimento: R\$ 7346.64
5      |
-----  | ---------------------------------
1000   |
0.06   | Valor final do investimento: R\$ 1191.02
3      |
-----  | ---------------------------------
20000  | 
0.04   | Valor final do investimento: R\$ 29604.89
10     |

### Fórmula do juros compostos:

![img](./img/juros-composto.gif)

### Código:


```python
valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

valor_final = valor_inicial * (1 + taxa_juros)**periodo

print("Valor final do investimento: R$", round(valor_final,2))
```

    20000
    0.04
    10
    Valor final do investimento: R$ 29604.89
    

[voltar](#ancora)

<a id="ancora5"></a>
## Desafio: O Grande Depósito

### Desafio
Você foi contratado por um banco para desenvolver um programa que auxilie seus clientes a realizar depósitos em suas contas. O programa deve solicitar ao cliente o valor do depósito e verificar se o valor é válido. Se o valor for maior do que zero, o programa deve adicionar o valor ao saldo da conta. Caso contrário, o programa deve exibir uma mensagem de erro e solicitar um novo valor. O programa deve continuar solicitando valores de depósito até que seja digitado um valor válido.

### Entrada
O programa deve utilizar o Scanner para receber os valores de depósito digitados pelo cliente. Os valores podem ser decimais, representando valores em reais.

### Saída
O programa deve exibir uma mensagem de sucesso quando um valor de depósito válido for informado e o saldo da conta for atualizado. Caso um valor inválido seja digitado, o programa deve exibir uma mensagem de erro e solicitar um novo valor.

### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Exemplo de Entrada | Exemplo de Saída
:-----------------:|:------------------:
500.50 | Deposito realizado com sucesso! Saldo atual: R$ 500.50
-----  | ---------------------------------
-100   | Valor invalido! Digite um valor maior que zero.
-----  | ---------------------------------
0      | Encerrando o programa...


```python
saldo = 0 

while True:
 try:
  valor = float(input())

  if valor > 0:
   saldo = saldo + valor
   print("Deposito realizado com sucesso!")
   print("Saldo atual: R$ {:.2f}".format(saldo))
   break
  
  elif valor == 0:
   print("Encerrando o programa...")
   break

  else:
   print("Valor invalido! Digite um valor maior que zero.")

 except EOFError:
  break
```

    500.50
    Deposito realizado com sucesso!
    Saldo atual: R$ 500.50
    

[voltar](#ancora)


```python

```

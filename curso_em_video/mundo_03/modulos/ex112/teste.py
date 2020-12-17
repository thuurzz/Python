"""
Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.
"""

from utilidadescev import moeda, dado


# Programa principal
p = dado.leiaDinheiro('Digite o valor R$: ')
txa = float(input('Digite o valor da taxa para aumento: '))
txd = float(input('Digite o valor da taxa para diminuição: '))
moeda.resumo(valor=p, vAumento=txa, vDecresc=txd)

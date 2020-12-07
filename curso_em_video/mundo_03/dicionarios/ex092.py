# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

import datetime

# Lê nome ano de nascimento e CTPS.
pessoa = {}
pessoa['Nome'] = input('Nome: ')
pessoa['Nascimento'] = int(input('Ano de nascimento: '))

# Cadastra as informações em um dicionário, deve ser cadastrada idade.
data_atual = datetime.date.today()
pessoa['Idade'] = data_atual.year - int(pessoa['Nascimento'])

# Se CTPS != de 0, pedir ano de contratação e salário.
pessoa['CTPS'] = int(input('CTPS, (0 se não tem): '))
if pessoa['CTPS'] != 0:
    pessoa['Ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: R$'))

    # Cadastrar com quantos anos vai se apodentar.
    pessoa['Ano aposentadoria'] = pessoa['Ano de contratação'] + 35
    pessoa['Idade aposentadoria'] = pessoa['Ano aposentadoria'] - pessoa['Nascimento']

# Exibe cadastro
print(f"{' CADASTRO ':=^50}")
for key, value in pessoa.items():
    print(f'- {key:.<20} tem o valor: {value:<10}')
print('=' * 50)
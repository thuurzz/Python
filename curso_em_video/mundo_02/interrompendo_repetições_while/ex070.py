# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print('=' * 20)
print('*LOJA DO ZECAURUBU TECH*')
print('=' * 20)

total = maisq_1k = cont = mais_barato = 0
nome_mais_barato = ''
while True:
    # contador de loops
    cont += 1
    # pede preço e nome
    nome_prd = input('Nome do prduto: ')
    preco_prd = float(input('Preço R$: '))
    # gasto TOTAL da compra.
    total += preco_prd
    # verifica produtos mais caros que R$ 1.000,00
    if preco_prd > 1000:
        maisq_1k += 1
    # verifica produto mais BARATO.
    if cont == 1:
        mais_barato = preco_prd
        nome_mais_barato = nome_prd
    if preco_prd < mais_barato:
        nome_mais_barato = nome_prd
    # pergunta se quer continuar
    opc = input('Deseja continuar? [S/N]').strip().upper()[0]
    while opc not in 'SN':
        opc = input('Use [S/N], deseja continuar? ').strip().upper()[0]
    if opc == 'N':
        break

# Mostrar gasto TOTAL da compra.
print(f'O valor total da compra é: {total:.2f}R$.')
# Mostrar quantos prdutos custam mais de R$ 1.000,00.
print(f'{maisq_1k} produtos dessa lista tem valor acima de R$ 1.000,00. ')
# Qual o nome do produto mais BARATO.
print(f'E o nome do produto mais barato foi: {nome_mais_barato}.')

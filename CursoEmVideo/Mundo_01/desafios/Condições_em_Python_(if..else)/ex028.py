import random

# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para
# o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o
# usuário venceu ou perdeu.Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá
# escrever na tela se o usuário venceu ou perdeu.

num = random.randint(0,5)

print('Foi gerado um número entre 0 e 5, tenta advinhar qual é! ')
chute = int(input('Faça seu lance: '))

if chute == num:
    print(f'Você acertou o número é: {num}')
else:
    print(f'Você errou o número era: {num}')
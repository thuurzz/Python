import random

# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para
# o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o
# usuário venceu ou perdeu.Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá
# escrever na tela se o usuário venceu ou perdeu.
# ++++++++++++++++++++++++++++++++++++++++++++++
#

# gera ńumero aleatório de 0 a 10
num = random.randint(0, 10)
tentativas = 1
print('Foi gerado um número entre 0 e 10, tenta advinhar qual é! ')

# Pede chute do usuário
chute = int(input('Faça seu lance: '))
if chute == num:  # se acertar, exibe resultado
    print(f'Você acertou o número é: {num}')
else:
    while not (chute == num):  # se errar, pede novamente
        tentativas += 1  # adiciona 1 ponto ao contador de tentativas
        print('Você errou!')
        chute = int(input('Faça seu lance novamente: '))

print(f'Você acertou o número em {tentativas} tentativas.')  # mostra quantidade de tentativas até acertar

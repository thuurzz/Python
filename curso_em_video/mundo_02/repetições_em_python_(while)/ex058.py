import random

# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para
# o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o
# usuário venceu ou perdeu.Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá
# escrever na tela se o usuário venceu ou perdeu.
# ++++++++++++++++++++++++++++++++++++++++++++++
# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram
# necessários para vencer.

# gera ńumero aleatório de 0 a 10
num = random.randint(0, 10)
tentativas = 1
print('Foi gerado um número entre 0 e 10, tenta advinhar qual é! ')
print(num)

# Pede chute do usuário
chute = int(input('Faça seu lance: '))
while not (chute == num):  # se errar, pede novamente
    tentativas += 1  # adiciona 1 ponto ao contador de tentativas
    print('Você errou!')
    if chute > num:
        print('Um pouco menos...')
    elif chute < num:
        print('Um pouco mais...')
    chute = int(input('Faça seu lance novamente: '))


print(f'Você acertou o número é: {num}')  # mostra que acertou
print(f'Você acertou o número em {tentativas} tentativas.')  # mostra quantidade de tentativas até acertar

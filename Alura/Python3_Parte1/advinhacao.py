import random

print(40 * '=')
print('Bem vindo ao Jogo de Advinhação!')
print(40 * '=')

numero_secreto = round(random.randrange(1,101))

total_tentativas = 3
rodada = 1

for rodada in range(1, total_tentativas + 1):
    print('Tentativa {}, de {}.'.format(rodada, total_tentativas))
    chute = int(input('Digite seu número dentro do intervalo de 1 até 100: '))
    if chute < 1 or chute > 100:
        print('você deve digitar um número entre 1 e 100!')
        continue

    print('Você digitou {}.'.format(chute))

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print('acertou miseravi!')
        break
    else:
        if maior:
            print('errou, seu número foi maior!')
        elif menor:
            print('errou, seu número foi menor! ')

    rodada += 1

print(f'Fim do jogo, o número era: {numero_secreto}.')

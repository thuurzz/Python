# advinhacao.py
import random

def jogar():
    print(40 * '=')
    print('Bem vindo ao Jogo de Advinhação!')
    print(40 * '=')

    numero_secreto = random.randrange(1, 101)  # gera número de 0 a 100

    pontos = 1000  # número inicial de pontos

    print('Qual o nível de dificuldade?')
    print('[1]Fácil [2] Médio [3]Difícil')

    nivel = int(input('Escolha seu nível de dificuldade: '))  # define o nível de dificuldade e qtd de chances
    while not 1 <= nivel <= 3:
        nivel = int(input('Escolha seu nível de dificuldade entre 1 e 3: '))  # define o nível de dificuldade e qtd de chances

    total_tentativas = 0
    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):  # inicia a rodada
        print('Tentativa {}, de {}.'.format(rodada, total_tentativas))
        chute = int(input('Digite seu número dentro do intervalo de 1 até 100: '))
        if chute < 1 or chute > 100:
            print('você deve digitar um número entre 1 e 100!')
            continue

        print('Você digitou {}.'.format(chute))

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:  # se acerta, encerra o jogo
            print(f'Acertou miseravi! Sua pontuação final é: {pontos}')
            break
        else:  # se não acerta, diz se foi maior ou menor
            if maior:
                print('Errou, seu número foi maior!')
                if rodada == total_tentativas:
                    print(f'O número secreto era {numero_secreto}. Você fez {pontos} pontos.')
            elif menor:
                print('Errou, seu número foi menor! ')
                if rodada == total_tentativas:
                    print(f'O número secreto era {numero_secreto}. Você fez {pontos} pontos.')
        pontos_perdidos = abs((numero_secreto - chute))
        pontos -= pontos_perdidos


if __name__ == '__main__':
    jogar()

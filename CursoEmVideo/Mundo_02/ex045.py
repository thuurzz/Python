import random

# Jokenpô!
# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
print('=' * 10)
print('JOKENPÔ')
print('=' * 10)


def jokenpo():
    jogador = int(input('Escolha:\n[1]Pedra\n[2]Papel\n[3]Tesoura\n'))
    jogador_joga = ''
    if jogador == 1:
        jogador_joga = 'Pedra'
    elif jogador == 2:
        jogador_joga = 'Papel'
    elif jogador ==3:
        jogador_joga = 'Tesoura'

    pc = random.randint(1,3)
    if pc == 1:
        pc_joga = 'Pedra'
    elif pc == 2:
        pc_joga = 'Papel'
    else:
        pc_joga = 'Tesoura'

    if jogador == pc:
        print(f'\033[7mJogador:{jogador_joga} + PC:{pc_joga} = Empate\033[m')
    elif (jogador == 1 and pc == 2) or (jogador == 2 and pc == 3) or (jogador == 3 and pc == 1):
        print(f'\033[7mJogador:{jogador_joga} + PC:{pc_joga} = PC Ganhou!\033[m')
    elif (jogador == 2 and pc == 1) or (jogador == 3 and pc == 2) or (jogador == 1 and pc == 3):
        print(f'\033[7mJogador:{jogador_joga} + PC:{pc_joga} = Jogador Ganhou!\033[m')


for i in range(5):
    jokenpo()

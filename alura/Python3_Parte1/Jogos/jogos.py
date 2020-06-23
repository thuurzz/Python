import forca
import advinhacao


def escolhe_jogo():
    print(25 * '=')
    print('===', 'Escolha seu jogo!', '===')
    print(25 * '=')
    print('[1] Advinhação [2] Forca')

    jogo = int(input('Qual jogo? '))
    while not 1 <= jogo <= 2:
        jogo = int(input('Escolha [1] ou [2]: '))
    if jogo == 1:
        print('Jocando Advinhação')
        advinhacao.jogar()
    elif jogo == 2:
        print('Jogando Forca')
        forca.jogar()


if __name__ == '__main__':
    escolhe_jogo()

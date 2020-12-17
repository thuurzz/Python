''''
Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
'''
c = (
    '\033[m',  # 0 -> SEM CORES
    '\033[0;30;41m',  # 1 -> VERMELHO
    '\033[0;30;42m',  # 2 -> VERDE
    '\033[0;30;43m',  # 3 -> AMARELO
    '\033[0;30;44m',  # 4 -> AZUL
    '\033[0;30;45m',  # 5 -> ROXO
    '\033[;7m'  # 6 -> INVERTE
)


def escreva(frase, cor=0):
    print(c[cor], end='')
    print('=' * 40)
    print(f'{frase:^40}')
    print('=' * 40)
    print(c[0], end='')


def ajuda(func):
    escreva(f'Acessando manual do comando <{func}>...', cor=4)
    print(c[6], end='')
    help(func)
    print(c[0], end='')


while True:
    escreva('SISTEMA DE AJUDA pyHELP', cor=3)
    print(c[2], end='')
    func = input('Função ou Biblioteca > ')
    print(c[0], end='')
    if func.upper() == 'FIM':
        break
    else:
        ajuda(func)
escreva('FIM DO PROGRAMA', cor=1)

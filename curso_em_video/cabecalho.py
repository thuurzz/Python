c =(
    '\033[m',              # 0 -> SEM CORES
    '\033[0;30;41m',       # 1 -> VERMELHO
    '\033[0;30;42m',       # 2 -> VERDE
    '\033[0;30;43m',       # 3 -> AMARELO
    '\033[0;30;44m',       # 4 -> AZUL
    '\033[0;30;45m',       # 5 -> ROXO
    '\033[7;30;m',         # 6 -> BRANCO
)


def escreva(frase, cor=0):
    print(c[cor], end='')
    print('=' * 40)
    print(f'{frase:^40}')
    print('=' * 40)
    print(c[0], end='')

#  SISTEMA PRINCIPAL

import time
from lib.arquivo import *
from lib.interface import *

# Cores para o terminal
cor = {
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'azul': '\033[1;34m',
    'ciano': '\033[1;36m',
    'magenta': '\033[1;35m',
    'amarelo': '\033[1;33m',
    'preto': '\033[1;30m',
    'branco': '\033[1;37m',
    'reset': '\033[1;0;0m',
    'reverso': '\033[1;2m',
    'bgpreto': '\033[1;40m',
    'bgvermelho': '\033[1;41m',
    'bgverde': '\033[1;42m',
    'bgamarelo': '\033[1;43m',
    'bgazul': '\033[1;44m',
    'bgmagenta': '\033[1;45m',
    'bgciano': '\033[1;46m',
    'bgbranco': '\033[1;47m'}


# Chama menu
while True:
    # 1 - Ver pessoas cadastradas
    # 2 - Cadastrar nova pessoa
    # 3 - Sair do programa
    opt = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Limpar cadastro', 'Sair do programa'])
    if opt == 1:
        mostraCadastro()
    elif opt == 2:
        cadastraPessoa()
    elif opt == 3:
        limpaCadastro()
    elif opt == 4:
        titulo('FIM DO PROGRAMA', txtCor="bgpreto")
        break
    else:
        print(f"{cor['vermelho']}ERRO: Digite uma opção válida!{cor['reset']}")
    time.sleep(1.3)

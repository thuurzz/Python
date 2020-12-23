import time

# Funções de leitra e impressão de dados

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


def linha(espaco=60):
    print('=' * espaco)


def titulo(msg, txtCor="branco"):
    linha()
    print(f'{cor[txtCor]}{msg:^60}{cor["reset"]}')
    linha()


def leiaInt(msg):
    while True:
        try:
            nInt = int(input(msg))
        except KeyboardInterrupt:
            print(f'\033[1;31mUsuário preferiu não informar dados.\033[0;0m')
            return 0
        except:
            print(f'\033[1;31mValor digitado inválido, tente novamente.\033[0;0m')
        else:
            return nInt


def menu(list):
    titulo('MENU PRICIPAL', txtCor="bgpreto")
    c = 1
    for opc in list:
        print(f'{cor["vermelho"]}{c} - {cor["reset"]}{cor["branco"]}{opc}{cor["reset"]}')
        c += 1
    linha()
    opt = leiaInt(f'{cor["verde"]}Digite a opção desejada: {cor["reset"]}')
    return opt


def cadastraPessoa():
    titulo('CADATRO DE PESSOAS', txtCor="bgpreto")
    # Abre arquivo para cadastro de nome e idade.
    with open('BDcadastro.txt', '+a') as cadastro:
        qtdCad = int(input('Quantidade de cadastros: '))
        for i in range(qtdCad):
            nome = input('Nome: ')
            idade = int(input('Idade: '))
            cadastro.write(f'ID:{i+1:0>4} | Nome: {nome:.<25} | Idade: {idade} \n')
    time.sleep(1)
    print(f'{cor["verde"]}Cadastro realizado com sucesso.{cor["reset"]}')
    linha()


def mostraCadastro():
    try:
        with open('BDcadastro.txt', 'r') as cadastro:
            txt = cadastro.read()
            titulo('CADASTRO', txtCor="bgpreto")
            print(txt)
            linha()
    except:
        print(f'{cor["vermelho"]} ERRO: Arquivo inexistente ou não encontrado.{cor["reset"]}')


def limpaCadastro():
    titulo('LIMPEZA DE CADASTRO', txtCor="bgpreto")
    while True:
        opt = input(f'{cor["vermelho"]}Tem certeza que deseja limpar cadastro:[S/N]{cor["reset"]}').strip().upper()[0]
        if opt in 'SN':
            break
    time.sleep(1)
    if opt == 'S':
        cadastro = open('BDcadastro.txt', 'w')
        cadastro.close()
        print(f'{cor["verde"]}Limpeza realizada com sucesso.{cor["reset"]}')
    else:
        print(f'{cor["vermelho"]}Operação cancelada.{cor["reset"]}')


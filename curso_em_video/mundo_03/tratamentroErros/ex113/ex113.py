'''
Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''


def leiaInt(msg):
    while True:
        try:
            nInt = int(input(msg))
        except (KeyboardInterrupt):
            print(f'\033[1;31mUsuário preferiu não informar dados.\033[0;0m')
            return 0
        except:
            print(f'\033[1;31mValor digitado inválido, tente novamente.\033[0;0m')
        else:
            return nInt


def leiaFloat(msg):
    while True:
        try:
            nFloat = float(input(msg))
        except (KeyboardInterrupt):
            print(f'\033[1;31mUsuário preferiu não informar dados.\033[0;0m')
            return 0
        except:
            print(f'\033[1;31mValor digitado inválido, tente novamente.\033[0;0m')
        else:
            return nFloat

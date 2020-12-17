'''
Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
'''
def leiaInt(caracteres):
    """Recebe uma entrada e verifica se é um número inteiro.

    Args:
        caracteres ([str]): [Frase que pede inteiro.]

    Returns:
        [int]: [Número inteiro recebido pelo input.]
    """
    while True:
        num = input(caracteres)
        if num.isnumeric():
            break
        else:
            print('ERRO! Digite um número inteiro válido!')
    return num


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')
'''
Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
'''

def ficha(nome = '<desconhecido>', gols = 0):
    """Mostra ficha do jogador cadastrado.

    Args:
        nome (str, optional): [Nome do jogador.]. Defaults to '<desconhecido>'.
        gols (int, optional): [Quantidade de gols.]. Defaults to 0.
    """
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


'''# Pede nome e gols
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    ficha(gols=g)
else:
    ficha(n, g)
'''

# Pede nome e gols
while True:
    n = str(input('Nome do jogador: '))
    if not n.isspace():
        break

while True:
    g = input('Número de gols: ')
    if g.isnumeric():
        g = int(g)
        break

ficha(nome=n, gols=g)


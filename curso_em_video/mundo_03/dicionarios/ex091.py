# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

import random
import time

# Quantidade de jogadores
nJog = 4

jogadores = {}
for i in range(nJog):
    jogadores[f'Jogador {i+1}'] = random.randint(1,6)

for jog, pt in jogadores.items():
    print(f'{jog} tirou {pt} no dado.')
    time.sleep(1)

# Exibe vencedor
print('-=' * 20)
print(f'{"RANKING DE JOGADORES":^40}')
print('-=' * 20)

ranking = sorted(jogadores.items(), key=lambda k: k[1], reverse=True)

cont = 1
for jog, pontos in ranking:
    print(f'{cont}* lugar: {jog} com {pontos}.')
    cont += 1

print('-=' * 20)
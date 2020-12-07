# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

# Lê nome do jogador e quantas partidas jogou
jogador= {}
jogador['Nome'] = str(input('Nome do jogador: '))
qtdPartidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

# Quantidade de gols para cada partida
gols = []
for i in range(qtdPartidas):
    gols.append(int(input(f'Quantidade de gols na partida {i+1}: ')))
jogador['Gols'] = gols

# Total de Gols nas partidas
jogador['Total de Gols'] = sum(jogador['Gols'])

# Mostra dict
print()
print(f"{' INFORMAÇÕES DO JOGADOR ':=^50}")
print(jogador)
print('=' * 50)
print()

# Mostra com for 
print(f"{' INFORMAÇÕES DO JOGADOR ':=^50}")
for key, value in jogador.items():
    print(f'O campo {key} tem o valor: {value}')
print('=' * 50)
print()

# Mostra com for formatado
print(f"{' INFORMAÇÕES DO JOGADOR ':=^50}")
print(f'Jogador {jogador["Nome"]}, jogou {qtdPartidas} partidas.')
for partida in range(qtdPartidas):
    print(f'=> Na partida {partida+1}, fez {jogador["Gols"][partida]} gols.')
print(f'Foi um total de {jogador["Total de Gols"]} de gols.')
print('=' * 50)

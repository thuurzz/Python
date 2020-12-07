# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

bdJogadores = []
jogador= {}
while True:
    # Lê nome do jogador e quantas partidas jogou
    jogador['Nome'] = str(input('Nome do jogador: '))
    qtdPartidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

    # Quantidade de gols para cada partida
    gols = []
    for i in range(qtdPartidas):
        gols.append(int(input(f'Gols na partida {i+1}: ')))
    jogador['Gols'] = gols

    # Total de Gols nas partidas
    jogador['Total de Gols'] = sum(jogador['Gols'])

    # Adiciona jogador ao Banco de Jogadores
    bdJogadores.append(jogador.copy())
    jogador.clear()

    # Pergunta se quer continuar
    while True:
        opc = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if opc in 'SN':
            break
    if opc == 'N':
        break

print(f"{' TABELA DE JOGADORES ':=^50}")
print(f'{"COD":<5}{"NOME":<10}{"GOLS":<20}{"TOTAL DE GOLS":>10}')
print(f"{'=' * 50}")
codJog = 0
for jogador in bdJogadores:
    print(f'{codJog:<5}{jogador["Nome"].upper():<12}{(str(jogador["Gols"])):<20}{jogador["Total de Gols"]:<15}')
    codJog += 1

while True:
    # Pede Id do jogador para mostrar informações
    idJog = int(input('Mostar dados de qual jogador? (999 para)'))
    if idJog == 999:
        break
    try:
        # Mostra informações do jogador selecionado
        print(f"{' INFORMAÇÕES DO JOGADOR ':=^50}")
        print(f'Jogador {bdJogadores[idJog]["Nome"]}.')
        # Exibe quantidade gols por partida do jogador
        for i in range(len(bdJogadores[idJog]["Gols"])):
            print(f'=> No jogo {i} fez {bdJogadores[idJog]["Gols"][i]} gols.')
        # Exibe total de gols nas partidas    
        print(f'Foi um total de {bdJogadores[idJog]["Total de Gols"]} de gols.')
        print('=' * 50)

    except IndexError:
        # Se ID não está na lista, pede de novo
        print(f'O ID deste jogador não conta na lista, tente novamente.')
print(f"{' FIM DO PROGRAMA ':=^50}")

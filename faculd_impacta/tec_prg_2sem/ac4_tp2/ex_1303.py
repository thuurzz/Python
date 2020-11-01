import numpy as np

# URI Online Judge | 1303
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1303

# Repete os testes até receber quantidade de times, ser 0.
instancia = 0
while True:
    n = int(input())
    if n ==0:
        break
    instancia += 1

    # Quantidade de partidas.
    part = n * (n-1) / 2
    
    # (lista com pontuação)
    pontGeral = [0] * n

    pontPartidas = [0] * n
    
    pontTomados = [0] * n

    for i in range(1, part + 1, 1):
        
        # Recebe dados, separa em vaiaveis.
        xyzw = input().split()
        # x primeiro time
        time1 = int(xyzw[0])
        # y pontos prim time
        pont1 = int(xyzw[1])
        # z segundo time
        time2 = int(xyzw[2])
        # w pontos seg time
        pont2 = int(xyzw[3])

        #contagem de vitorias
        if pont1 > pont2:
            pontGeral[time1-1] += 2
            pontGeral[time2-1] += 1
        else:
            pontGeral[time1-1] += 1
            pontGeral[time2-1] += 2\
        
        #pontos feitos por partida
        pontPartidas[time1-1] += pont1
        pontPartidas[time2-1] += pont2

        #pontos tomados por partida
        pontTomados[time1-1] += pont2
        pontTomados[time2-1] += pont1

    #calcular colocacao no campeonato
    empates = [
        [0, 5],
        [2, 6],
        [2, 7]
    ]
    for indPont in range(len(pontGeral)):
        naoEmpatou = True
        for checkPont in range(indPont,len(pontGeral)):
            if (indPont != checkPont) and pontGeral[indPont] == pontGeral[checkPont]:
                if naoEmpatou:
                    empates.append([indPont, checkPont])
                    naoEmpatou = False
                else:
                    empates[-1].append(checkPont)

    


    

# Separa vitoria 

# se empata no campeonato, sort(“cesta average”) (na improvável hipótese de um time vencer todos os jogos do campeonato sem levar cestas seu cesta average é dado pelo número de pontos marcados)

# se ainda empate, marca maior pontos totais

# Ainda havendo empate, o time com menor número de inscrições na liga ﬁca na frente.

# Time com id maior, tem vantangem  

#le qto times

# qtade de jogos e resultados n (n−1) / 2

# ENTRADA

# x primeiro time
# y pontos prim time
# z segundo time
# w pontos seg time


# VARIAVEIS
# lista ponto do camp por vitória
# lista pontos marcados (cestas em todas as partidas)
# lista pontos recebidos (cestas em todas as partidas)


# SAIDA
# imprimir um identiﬁcador "Instancia h" 
# imprimir num identificador times em ordem de vitoria

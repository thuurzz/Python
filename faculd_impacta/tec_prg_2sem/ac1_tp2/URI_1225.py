# URI Online Judge | 1125

while True:
    # recebe em uma linha, separa
    # print("Olá! Vamos verificar os campeões de um novo campeonato para vários sistemas de pontos!")
    # print("Digite o numero de GPs (corridas) e o total de pilotos:\n")
    g, p = input().split()
    if g != '0' and p != '0':
        # número de Grandes Prêmios (corridas nesse campeonato) (1 ≤ G ≤ 100)
        g = int(g)
        # número de pilotos nesse campeonato(1 ≤ P ≤ 100)
        p = int(p)

        #print("Digite os resultados de cada um dos GPs:\n")
        # lê a posição de chegada dos pilotos em cada corrida
        lista_corridas = []
        for i in range(g):
            lchegada = [int(n) for n in input().split()]
            lista_corridas.append(lchegada)
            
        # lê número inteiro S indicando a quantidade de sistemas de pontuação (1 ≤ S ≤ 10)
        # print("Digite a quantidade de sistemas de pontuação a serem usados:\n")
        s = int(input())
        lista_sistemas = []
        # print("Digite a descrição de cada sistema de pontuação:")
        # print("(nº de pilotos pontuados nesse sistema) ([lista de pontuação de cada piloto por posição])\n")
        for i in range(s):
            # A descrição de um sistema de pontuação inicia com um inteiro K (1 ≤ K ≤ P) de pilotos pontuados
            pont = [int(n) for n in input().split()]
            lista_sistemas.append(pont)
        # a partir deste ponto, temos tudo o que precisamos para encontrar os campeões em cada sistema

        # para cada sistema de pontuação, calcule o(s) campeão(ões) para aquele sistema e imprima na tela:
        for sis in lista_sistemas:
            # popula com 0 inicial pontuação de cada piloto
            pontuacoes_pilotos = [0] * p
            for corrida in lista_corridas:
                # calcular pontuacoes de cada piloto
                # oq quero no final: uma lista onde cada posição corresponde à pontuação daquele piloto daquele indice
                for idx_piloto in range(len(corrida)):
                    #checar se este piloto será pontuado, se sim, pontue-o corretamente
                    #corrida[idx_piloto] == é a colocação do piloto atual na corrida atual
                    #sis[ corrida[idx_piloto] ] == é a quantidade de pontos que o piloto nesta colocação x deve receber
                    if corrida[idx_piloto] <= sis[0]:
                        pontuacoes_pilotos[idx_piloto] += sis[ corrida[idx_piloto] ]

            #aqui terei em pontuacoes_pilotos as pontuações de cada piloto
            campeoes = []
            maximo = max(pontuacoes_pilotos)
            for idx_piloto in range(len(pontuacoes_pilotos)):
                if pontuacoes_pilotos[idx_piloto] == maximo:
                    campeoes.append(str(idx_piloto + 1))
            # print("Campeões do campeonato no sistema", sis)
            print(' '.join(campeoes))
    else:
        break
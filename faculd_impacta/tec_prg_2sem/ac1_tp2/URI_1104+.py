# URI Online Judge | 1104

# pede número de cartas por lista
while True:
    num_cartas = []
    n = input().split()
    for i in n:
        num_cartas.append(int(i))

    # se o numero != de  0 0 inicia sequência
    if (num_cartas[0] and num_cartas[1]) != 0:
        c_alice = set()
        c_beatriz = set()
        # lê sequencias da Alice, retira os repetidos
        list_cartas_a = input().split()
        for n in list_cartas_a:
            c_alice.add(int(n))
                
        # lê sequencias da Beatriz, retira os repetidos
        list_cartas_b = input().split()
        for n in list_cartas_b:
            c_beatriz.add(int(n))
        
        # verifica quais estão disponíveis para troca, coloca na lista        
        dif_ab = c_alice - c_beatriz
        dif_ba = c_beatriz - c_alice

        # verifica qual número menor e coloca o tamanho na var
        n_max_troc = 0
        if len(dif_ab) < len(dif_ba):
            n_max_troc = len(dif_ab)
        else:
            n_max_troc = len(dif_ba)

        # exibe valor
        print(f'\033[7m{n_max_troc}\033[0m')
    else:
        break


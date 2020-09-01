# URI Online Judge | 1104

# pede número de cartas por lista
while True:
    num_cartas = []
    n = input().split()
    for i in n:
        num_cartas.append(int(i))
    # se o numero != de  0 0 inicia sequência
    if (num_cartas[0] and num_cartas[1]) != 0:
        cartas_a = []
        cartas_b = []
        cartas_a_limpo = []
        cartas_b_limpo = []
        
        # lê sequencias da Alice, retira os repetidos
        list_cartas_a = input().split()
        for n in list_cartas_a:
            cartas_a.append(int(n))
            for n in cartas_a:
                if n not in cartas_a_limpo:
                    cartas_a_limpo.append(int(n))
        
        # lê sequencias da Beatriz, retira os repetidos
        list_cartas_b = input().split()
        for n in list_cartas_b:
            cartas_b.append(int(n))
            for n in cartas_b:
                if n not in cartas_b_limpo:
                    cartas_b_limpo.append(int(n))

        # verifica quais estão disponíveis para troca, coloca na lista        
        disp_troca_ab = []
        for n in cartas_a_limpo:
            if n not in cartas_b_limpo:
                disp_troca_ab.append(n)

        disp_troca_ba = []
        for n in cartas_b_limpo:
            if n not in cartas_a_limpo:
                disp_troca_ba.append(n)

        # verifica qual número menor e coloca o tamanho na var
        n_max_troc = 0
        if len(disp_troca_ab) < len(disp_troca_ba):
            n_max_troc = len(disp_troca_ab)
        elif len(disp_troca_ab) > len(disp_troca_ba):
            n_max_troc = len(disp_troca_ba)

        # exibe valor
        print(f'\033[7m{n_max_troc}\033[0m')
    else:
        break


# URI Online Judge | 1266

while True:
    # total de postes
    tot_postes = int(input())
    if tot_postes != 0:
        #lista contém ou não postes
        l_postes = [int(n) for n in input().split()]
        pm = 0
        for i in range(len(l_postes) - 1):
            # confere o primeiro, o segundo e o último postes forem 0, troca o primeiro para 1
            if i == 0:
                #print("Estou no primeiro! l_postes:")
                #print(l_postes)
                if l_postes[i] == 0 and l_postes[i + 1] == 0 and l_postes[i + 2] == 0:
                    #print('entrei!')
                    l_postes[i + 1] = 1
                    pm += 1
                elif l_postes[i] == 0 and l_postes[i + 1] == 0 and l_postes[i + 2] == 1:
                    continue

            if l_postes[i] + l_postes[i + 1] == 0:
                l_postes[i + 1] = 1
                pm += 1
        if l_postes[-1] == 0 and l_postes[0] == 0:
                l_postes[0] = 1
                pm += 1
        if l_postes[0] == 0 and l_postes[1] == 0:
                l_postes[0] = 1
                pm += 1
        print(pm)
    else:
        break
# URI Online Judge | 1211
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1211

# inicia o looping até EOFError

def selection_sort(vet):
    for i in range(len(vet) - 1):
        p = i
        for j in range(i + 1, len(vet)):
            if vet[j] < vet[i]:
                p = j
            vet[i], vet[p] = vet[p], vet[i]
        

def qsort(vet):
    if len(vet) > 1:
        vet2 = [x for x in vet[1:] if x < vet[0]]
        vet3 = [x for x in vet[1:] if x >= vet[0]]
        vet = qsort(vet2) + vet[:1] + qsort(vet3)
    return vet


while True:
    try:
        # Quantidade de telefones
        n = int(input())

        # Inicia lista e adiciona telefones
        lTel = []
        for i in range(n):
            tel = input()
            lTel.append(tel)
            # implementar algoritmo de ordenação mais eficiente
            lTel.sort() #Time limit exceeded 
            #selection_sort(lTel) #Time limit exceeded 
            #lTel = qsort(lTel) #Time limit exceeded 

        econ = 0
        # Passeia pela lista de telefones.
        for i in range(1, len(lTel), 1):
            # Passeia pelos caracteres.
            for j in range(len(lTel[0])):
                # verifica se o primeiro caractere do de cima e de baixo, são iguais.
                if lTel[i][0] == lTel[i-1][0]:
                    # Tendo primeiro caractere igual, testa os outros.
                    if lTel[i][j] == lTel[i-1][j]:
                        # Cada caractere igual, que não será impresso, adiciona +1 para a acumuladora.
                        econ += 1
                    else:
                        # Se identificar caractere diferente, para e vai pro próximo.
                        break
        # Exibe quantidade de caracteres economizados a cada loop
        print(econ)
    except EOFError:
        break


'''
Caso teste que falha
4
11112222
22221111
22223333
11111111
8 (Resultado)

6
123456
123465
123546
123564
123645
123654
18 (Resultado)
'''
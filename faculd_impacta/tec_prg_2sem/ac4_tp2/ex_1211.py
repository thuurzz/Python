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
            #lTel.sort()
            selection_sort(lTel)

        econ = 0
        # Passeia plea lista de telefones
        for i in range(len(lTel) - 1):
            # Passeia pelos caracteres
            for tel in range(len(lTel[i])):
                # verifica se o primeiro caractere do de cima e de baixo, são iguais
                if lTel[i][0] == lTel[i + 1][0]:
                    # Tendo primeiro caractere igual, testa os outros
                    if lTel[i][tel] == lTel[i + 1][tel]:
                        # Cada caractere igual, que não será impresso, adiciona +1 para a acumuladora
                        econ += 1
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
4 (Deveria dar 8)
'''
def cria_matriz(linhas, colunas, preenchimento):
    matriz = [] #inicia a matriz vazia
    for i in range(linhas): #repete até o num de linhas
        linha = colunas * [preenchimento] #preenche as colunas
        matriz.append(linha) #adiciona linhas na matriz
    return matriz #retorna a matriz


def imprime_matriz(A):
    linha = len(A)
    coluna = len(A[0])
    for i in range(linha):
        for j in range(coluna):
            print("%7.2f" % A[i][j], end='')
        print()


def preenche_matriz(matriz):
    linha = len(A)
    coluna = len(A[0])
    for i in range(linha):
        for j in range(coluna):
            matriz[i][j] = int(input("Posição [%d][%d]: " % (i, j)))
    return matriz


A = cria_matriz(3,3,2)
print('Antes:')
imprime_matriz(A)

print('Depois:')
imprime_matriz(A)

#percorre e checa valores usando coordenadas
pares = 0
linha = len(A)
coluna = len(A[0])
for i in range(linha):
    for j in range(coluna):
        if A[i][j] % 2 == 0:
            pares += 1
print(f'Esta matriz tem {pares} números pares')


#explo de percorrer matriz por iteração, item por item.
'''
A = cria_matriz(3,3,2)
pares = 0
imprime_matriz(A)
for linha in A:
    for valor in linha:
        if valor % 2 == 0:
            pares +=1
print(f'Esta matriz tem {pares} números pares')
'''

def cria_matriz(m, n, valor):
    """
    m: número de linhas
    n: número de colunas
    valor: valor inicial
    """
    matriz = []
    for i in range(m):
        linha = [valor] * n
        matriz.append(linha)
    return matriz

def imprime_matriz(A):
    lin_a = len(A)
    col_a = len(A[0])
    for i in range(lin_a): # i varia de 0 até lin_a - 1
        for j in range(col_a): # j varia de 0 até col_a - 1
            print("%7.2f" % A[i][j], end='')
        print() # força um "pula linha" para cada linha da matriz

# Programa principal:
A = cria_matriz(3, 5, 0)
print("Antes:")
imprime_matriz(A)
print("Depois:")
A[0][1] = 135
A[1][2] = 352
imprime_matriz(A)

#Arthur Vinicius Santos Silva RA:1903365
#professor, trabalho de fds, não terminei por completo, irei revisar!
def cria_matriz(linhas, colunas, preenchimento):
    matriz = [] #inicia a matriz vazia
    for i in range(linhas): #repete até o num de linhas
        linha = colunas * [preenchimento] #preenche as colunas
        matriz.append(linha) #adiciona linhas na matriz
    return matriz #retorna a matriz

def preenche_matriz(matriz):
    linha = len(A)
    coluna = len(A[0])
    for i in range(linha):
        for j in range(coluna):
            matriz[i][j] = input("Posição [%d][%d]: " % (i, j))
    return matriz

m = int(input('Informe a quantidade de Alunos: \n'))
n = 6
A = cria_matriz(m,n,0)
preenche_matriz(A)

maior_media = -1
linha_maior_med = -1
for i in A:
    print(f'Aluno {A[i][0]}')
    for j in i:
         print(f'nota {A[i][j + 1]}')
    media = sum(A[i][1:n]) / (n - 1)
    print(f'Média: {media}')
    print()
    if media > maior_media:
        maior_media = media
        linha_maior_med = i

print(f'O aluno, {A[linha_maior_med[0]]} tem a maior média {maior_media}.')

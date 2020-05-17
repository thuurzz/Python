#Arthur Vinicius Santos Silva RA:1903365


def cria_matriz(linhas, colunas, preenchimento):
    matriz = [] #inicia a matriz vazia
    for i in range(linhas): #repete até o num de linhas
        linha = colunas * [preenchimento] #preenche as colunas
        matriz.append(linha) #adiciona linhas na matriz
    return matriz #retorna a matriz


def preenche_matriz(matriz):
    for i in range(m):
        matriz[i][0] = input('Digite o nome do aluno:')
        for j in range(1, n):
            matriz[i][j] = float(input(f"Digite a nota {j} do Aluno:"))
    return matriz


m = int(input('Informe a quantidade de Alunos: \n'))
n = 3
A = cria_matriz(m,n,0)
preenche_matriz(A)

print('\n')

maior_media = -1
linha_maior_med = -1

for i in range(m):
    print(f'Aluno: {A[i][0]}')
    for j in range(1, n):
        print(f'Nota {j}: {A[i][j]}')
    soma = sum(A[i][1:n])
    media = soma / (n - 1)
    print(f'Média: {media}')
    print()
    if media > maior_media:
        maior_media = media
        linha_maior_med = i

print(f'O aluno, {A[linha_maior_med][0]} tem a maior média: {maior_media}')

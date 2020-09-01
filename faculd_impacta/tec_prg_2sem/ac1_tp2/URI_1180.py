# URI Online Judge | 1180

# lê tamanho do vetor, cria.
n = int(input())
X = n * [0]

# lê entrada como string, separa pelo ' ' co  .split()
X = input().split()

# loop que itera string do input e cria lista de inteiros
for n in range(len(X)):
    X[n] = int(X[n])

# pega menor valor da lista
menor = min(X)
# pega indice do menor valor da lista
indice = X.index(min(X))

# exibe valores
print(f'''Menor valor: {menor}
Posicao: {indice}''')

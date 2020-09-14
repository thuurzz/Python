# URI Online Judge | 1238

# Lê quantidade de repetições
n = int(input())

for i in range(n):
    # lê palavras e separa
    palavras = input().split()
    combPlvr = []
    # pega qual das palavras é maior
    maior = max(len(palavras[0]), len(palavras[1]))
    # enquanto o contador for menor que a tamanho da palavra, adiciona alternadamente as letras para uma nova lista
    for i in range(maior):
        if i < len(palavras[0]):
            combPlvr.append(palavras[0][i])
        if i < len(palavras[1]):
            combPlvr.append(palavras[1][i])
    # exibe lista com junção das letras
    print(''.join(combPlvr))


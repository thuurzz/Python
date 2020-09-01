# URI Online Judge | 1176

# lê número de casos
caso = int(input())

# repete a quantidade de vezes lida
for i in range(caso):
    # lê a posição do número fibonacci a ser exibido 
    # e até onde sera gerada sequência
    nf = int(input())

    # cria vetor com 2 valores iniciais fibonacci
    sfib = [0, 1]

    # loop cria fibonacci
    for i in range(nf):
        sfib.append(sfib[i] + sfib[i + 1])

    # exibe valor fibonacci correspondente ao indice solicitado
    print(f'Fib({nf}) = {sfib[nf]}')



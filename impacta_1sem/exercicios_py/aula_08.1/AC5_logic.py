# Criar uma função que recebe um vetor de inteiros como parâmetro e retorna o índice do último elemento ímpar do vetor.
# Lucas da Silva Santos RA: 1904209
# Arthur Vinicius Santos Silva RA: 1903665
# Brasilio Soares de Campos Neto RA: 1902861


def impar(lista):
    cont = len(lista)
    p = 0
    ind = 0
    ip = 0
    for i in range(cont):
        if lista[i] % 2 != 0:
            ind = i
    return ind


v = eval(input())

print("indice do ultimo impar ", impar(v))

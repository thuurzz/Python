# Criar uma função que recebe um vetor de inteiros como parâmetro e retorna o índice do último elemento ímpar do vetor.

def indice_ult_impar(lista):
    impares = 0
    for i in range(len(lista)):
        if lista[i] % 2 != 0:
            impares = i
    return impares


lista = eval(input())
print(f'Indice do ultimo impar {indice_ult_impar(lista)}')



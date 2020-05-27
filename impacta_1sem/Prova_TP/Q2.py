# Escreva um algoritmo (pode ser em fluxograma ou em Python) com uma função que recebe por parâmetro um
# vetor com uma quantidade qualquer de números inteiros e retorna o índice em que se encontra o menor
# elemento da lista.

#recebe lista de inteiros e verifica o inidice do menor
def indice_menor_do_vetor(vetor):
    ind_menor = -1
    menor = vetor[0]
    for i in range(len(vetor)):
        if vetor[i] <= menor:
            menor = vetor[i]
            ind_menor = i
    return ind_menor


vetor = eval(input('Digite uma lista de números inteiros sem os repetir: '))
indice_menor = indice_menor_do_vetor(vetor)

print(f'O indice do menor elemento é: {indice_menor}.')

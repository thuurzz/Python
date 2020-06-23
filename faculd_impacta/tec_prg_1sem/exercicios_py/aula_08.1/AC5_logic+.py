# Criar uma função que recebe um vetor de inteiros como parâmetro e retorna o índice do último elemento ímpar do vetor.


def indice_ult_impar(lista): #cria função
    impares = 0 #inica var para receber indice
    for i in range(len(lista)): #itera todos os itens da lista
        if lista[i] % 2 != 0: #verifica se é impar
            impares = i #se é impar, o valor do i(que no caso é o indice) é atribuido na variavel
    return impares #retorna ultimo indice que foi atribuido


lista = eval(input()) #recebe valores, coloca na lita
print(f'Indice do ultimo impar {indice_ult_impar(lista)}') #mostra valor



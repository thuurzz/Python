# Arthur Vinicius Santos Silva RA:1903365
# Faça um programa onde o usuário digita 4 números e ele printa na tela o valor do maior vezes o menor.
# Obs: Para isso crie 3 funções: uma que retorna o menor entre 4 números; uma que retorna o maior entre 4 números;
# e uma que usa as funções anteriores para retornar o maior vezes o menor.

import sys


def mostra_maior():
    maior = 0
    for i in range(4):
        n = int(input())
        if n > maior:
            maior = n

        print(maior)
    return maior


def mostra_menor():
    menor = sys.maxsize
    for i in range(4):
        n = int(input())
        if n < menor:
            menor = n
        print(menor)

    return menor


def mostra_mult_menor_maior():
    n1 = mostra_maior()
    n2 = mostra_menor()
    print(n1)
    print(n2)

    mult = n1 * n2
    print(mult)

    return mult


mult = mostra_mult_menor_maior()
print(mult)



# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

# ex100
import random

# Lista para trabalho
nSorteados = []

def sorteia(list):
    """
    Sorteia 5 números e coloca dentro da lista.

    Args:
        list ([int]): [lista de números sorterados.]
    """
    while len(list) < 5:
        n = random.randint(0,10)
        if n not in list:
            list.append(n)
    list.sort()
    print(f'Foram adicionados os valores a lista: {nSorteados}')


def mostraMaior(list):
    """
    Recebe lista e mostra maior.

    Args:
        list ([int]): [lista de números sorterados.]
    """
    maior = 0
    for i,v in enumerate(list):
        if i == 0:
            maior = v
        else:
            if v > maior:
                maior = v
    print(f'Na lista {list} o maior valor é: {maior}')
    

def somaPar(list):
    """Recebe lista de números e mostra soma dos pares 

    Args:
        list ([int]): [lista de números sorterados.]
    """
    soma = 0
    print('Os números pares da lista são:')
    for num in list:
        if num % 2 == 0:
            soma += num
            print(num, end=' ')
    print(f'e sua soma vale {soma}.')



sorteia(nSorteados)
mostraMaior(nSorteados)
somaPar(nSorteados)

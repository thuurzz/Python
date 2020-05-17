# Escreva a funcao media_pares_impares(lista) abaixo:
# Arthur Vinicius Santos Silva   RA:1903365
def media_pares_impares(lista):
    impares_da_lista = []
    pares_da_lista = []
    for i in lista:
        if i % 2 == 0:
            pares_da_lista.append(i)
        else:
            impares_da_lista.append(i)

    print(sum(pares_da_lista) / len(pares_da_lista)) # média dos números pares contidos na lista
    print(sum(impares_da_lista) / len(impares_da_lista)) # média dos números pares contidos na lista

# Programa principal (ja implementado, voce nao precisa se preocupar com o codigo partir deste ponto)
lista = eval(input())
media_pares_impares(lista)

'''
[12, 13, 35, 77, 68, 6, 11, 94, 7, 88]
'''

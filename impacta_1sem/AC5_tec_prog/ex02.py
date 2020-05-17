# Escreva a funcao interseccao(lista1, lista2) abaixo:
# Arthur Vinicius Santos Silva   RA:1903365
def interseccao(lista1, lista2):
    lista_interseccao = []
    for i in range(len(lista1)):
        if lista1[i] in lista2:
            lista_interseccao.append(lista1[i])

    for i in range(len(lista_interseccao)):
        if lista_interseccao.count(lista_interseccao[i]) > 1:
            #lista_interseccao.pop(lista_interseccao[i])

            lista_interseccao.sort()
    return lista_interseccao

# Programa principal (ja implementado, voce nao precisa se preocupar com o codigo partir deste ponto)
lista1 = eval(input())
lista2 = eval(input())
resultado = interseccao(lista1, lista2)
if isinstance(resultado, list):
    print(resultado)
else:
    print("Erro. Voce deve devolver uma lista")

'''
[10, 11, 14, 20, 8, 2, 14, 3, 11]
[1, 10, 9, 14, 20, 14]
'''

# Escreva a funcao interseccao(lista1, lista2) abaixo:
# Arthur Vinicius Santos Silva   RA:1903365
def interseccao(lista1, lista2):
    lista_interseccao = [] #lista vazia
    for i in range(len(lista1)): #percorre a lista
        if lista1[i] in lista2: #verifica se os itens da lista 1 estão na 2
            lista_interseccao.append(lista1[i]) #adiciona os que estão nas 2 em outra

        list_intersec_sem_duplicados = [] #cria lista vazia
        for i in lista_interseccao: #percorre a lista
            if i not in list_intersec_sem_duplicados: #se não esta na lista, adiciona
                list_intersec_sem_duplicados.append(i) #adiciona a lista

            list_intersec_sem_duplicados.sort() #coloca em ordem crescente
    return list_intersec_sem_duplicados

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

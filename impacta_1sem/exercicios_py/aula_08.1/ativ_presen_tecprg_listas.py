# Arthur Vincius Santos Silva RA: 1903665


# Escreva um programa em Python que lê e percorre uma string de 2 em 2 caracteres a partir do
# primeiro e os exibe (imprime) na tela.


def imprime2_em_2(str):
    palavra2_2 = ''
    for i in range(0, len(str), 2):
        palavra2_2 += str[i]

    print(palavra2_2)


def ocorrencias1(lst, x):
    tem_na_lista = 0
    tamanho = len(lst)

    for i in range(tamanho):
        if x == lst[i]:
            tem_na_lista += 1

    return tem_na_lista


lista = [8, 9, 10, 6, 5, 3, 8, 7, 8, 3, 8]
x = 8

opcao = input('Escolha: \n[1] Digite uma palavra e serão exibidos carateres de 2 em 2: \n[2] Exibe quantas ocorrências do número 8 tem na lista:\n')
if opcao == 1:
    palavra = input('Digite uma palavra e serão exibidos carateres de 2 em 2:\n')
    imprime2_em_2(palavra)
else:
    o = ocorrencias1(lista, x)
    print(o)

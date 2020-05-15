#Arthur Vincius Santos Silva RA: 1903665
#irei revisar o ex depiois.

'''
def imprime2_em_2(str):
    for i in range(0, len(str), 2):

    print(str, end=””)
'''

def ocorrencias1(lst, x):
    tem_na_lista = 0
    tamanho = len(lst)
    for i in range(tamanho):
        if x in lst:
            tem_na_lista += 1

    return tem_na_lista

palavra = input('')

#imprime2_em_2(palavra)


l = [1,2,3,3,2]
x = 3

o = ocorrencias1(l, x)
print(o)



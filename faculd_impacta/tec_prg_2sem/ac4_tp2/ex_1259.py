# URI Online Judge | 1259
#OK
lista_impar = []
lista_par = []

def imp_impar(l):
    l.sort(reverse=True)
    for item in l:
        print(item)


def imp_par(l):
    l.sort()
    for i in range(len(l)):
        print(l[i])

# repete quantas vezes entrar em quantidade
qtde = int(input())
for i in range(qtde):
    n = int(input())
    if n % 2 == 0 and n>0:
        lista_par.append(n)
    elif  n % 2 != 0 and n>0:
        lista_impar.append(n)
    

imp_par(lista_par)
imp_impar(lista_impar)


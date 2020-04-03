""" 
#apenas IfElse

n1 = float(input('Informe um número: '))
n2 = float(input('Informe outro número: '))

if n1 > n2:
    maior = n1
    menor = n2

else:
    maior = n2
    menor = n1

diferenca = (maior - menor)
print(diferenca)
"""

""" 
#IfElse como função

def difereca_maior_menor():
    n1 = float(input('Informe um número: '))
    n2 = float(input('Informe outro número: '))

    if n1 > n2:
        maior = n1
        menor = n2

    else:
        maior = n2
        menor = n1

    diferenca = (maior - menor)
    print(diferenca)


difereca_maior_menor()


"""
#IfElse com parametros

def difereca_maior_menor(n1 , n2):
    if n1 > n2:
        maior = n1
        menor = n2

    else:
        maior = n2
        menor = n1

    diferenca = (maior - menor)
    print(diferenca)

# Programa pricipal:
n1 = float(input('Informe um número: '))
n2 = float(input('Informe outro número: '))

difereca_maior_menor(n1, n2)









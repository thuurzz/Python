# URI Online Judge | 1171

# quantidade de números para testar
n = int(input())

lista = []
setList = set()
for i in range(n):
    alg = int(input())
    lista.append(alg)

setList = set(lista)
for item in setList:
    print(f'{item} aparece {lista.count(item)} vez(es)')
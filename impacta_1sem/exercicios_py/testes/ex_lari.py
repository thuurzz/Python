def interseccao(lista1, lista2):
    final = []
    aux = 0
    m = 0
    n = 0

    m = len(lista1)
    n = len(lista2)

    for i in range(m):
        for j in range(n):
            if lista1[i] == lista2[j]:
                aux = lista1[i]
                final.append(aux)

    final2 = []
    for item in final:
        if item not in final2:
            final2.append(item)

    final2.sort()
    return final2


a = [10, 11, 14, 20, 8, 2, 14, 3, 11]
b = [1, 10, 9, 14, 20, 14]

x = interseccao(a, b)
print(x)


for item in a:
    print(item)

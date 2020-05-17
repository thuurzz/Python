# Exibe maior da lista

def maior_da_lista(l):
    list.sort(l)
    ultimo = len(l) - 1
    m = l[ultimo]
    return m


n = [2, 3, 5, 7, 9]

x = maior_da_lista(n)
print(x)

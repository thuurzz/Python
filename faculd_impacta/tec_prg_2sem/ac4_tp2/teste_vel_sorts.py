import time

def selection_sort(vet):
    for i in range(len(vet) - 1):
        p = i
        for j in range(i + 1, len(vet)):
            if vet[j] < vet[i]:
                p = j
                vet[i], vet[p] = vet[p], vet[i]
    return vet


def qsort(vet):
    if len(vet) > 1:
        vet2 = [x for x in vet[1:] if x < vet[0]]
        vet3 = [x for x in vet[1:] if x >= vet[0]]
        vet = qsort(vet2) + vet[:1] + qsort(vet3)
    return vet


y = [50, 28, 73, 87, 37, 31, 17, 21, 61, 57, 66, 11, 93, 47, 82]

inicio = time.time()
# Selection Sort
y = selection_sort(y)
print(f'Lista Selection Sort:{y}')
final = time.time()
tempo = inicio - final
print(f'{final:.6f}')

inicio = time.time()
# Quick Sort
y = qsort(y)
print(f'Lista Quick Sort:{y}')
final = time.time()
tempo = inicio - final
print(f'{final:.6f}')


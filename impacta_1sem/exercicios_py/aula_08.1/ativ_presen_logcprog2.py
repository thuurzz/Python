#Arthur Vincius Santos Silva RA:1903665
#Contador de ocorrências na lista
def cont(vetor, x):
    tam = (len(vetor))
    conta = 0
    for item in range(tam):
        if vetor[item] == x:
            conta += 1
    return conta


lista = []
print('digite 5 valores para criar uma lista: ')
for i in range(5):
    n = int(input(f'digite o número da posição {i + 1}: '))
    lista.append(n)

x = int(input('escolha um número para ser buscado na lista: '))

ocorrencias = cont(lista, x)
print('')
print(f'O número {x}, tem {ocorrencias} ocorrências na lista!')

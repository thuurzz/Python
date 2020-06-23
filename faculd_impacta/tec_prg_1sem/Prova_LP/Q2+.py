#recebe lista de inteiros e verifica o índice do menor
def indice_menor_do_vetor(vetor):
   ind_menor = -1
   menor = vetor[0]
   for i in range(len(vetor)):
       if vetor[i] <= menor:
           menor = vetor[i]
           ind_menor = i
   return ind_menor

vetor = []
print('Digite uma sequência de números inteiros, o índice do menor sera exibido, quando terminar de digitar a lista, digite : ok.')
while True:
    n = input('Digite um número inteiro: ')
    if n == 'ok':
        break
    else:
        n = int(n)
        vetor.append(n)

indice_menor = indice_menor_do_vetor(vetor)

print(f'O índice do menor elemento da lista {vetor} é: {indice_menor}.')

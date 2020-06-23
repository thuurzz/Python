#Arthur Vincius Santos Silva RA: 1903365

# 1) Dada a seguinte lista: lst = ['cereal', 'banana', 'maçã', 'melão','iogurte']
lst = ['cereal', 'banana', 'maçã', 'melão', 'iogurte']

# a) Escreva uma função imprime_lista(lista), que recebe uma lista como parâmetro e
# imprime (percorre) todos os elementos da lista, juntamente com o seu respectivo índice. Use uma
# estrutura de repetição para isso. Exemplo da execução desta função:
# 0 - cereal
# 1 - banana
# 2 - maçã
# e assim por diante....
def imprime_lista(lista):
    for i in range(len(lst)):
        print(f'{i} - {lst[i]}')
# b) Na sequência (no programa principal), imprima o tamanho da lista.
'''
print(len(lst))
'''
# c) Em seguida, imprima (no programa principal) o elemento no índice 3 da lista.
'''
print(lst[3])
'''
# d) Ainda no programa principal, leia uma entrada do usuário (como string), e insira este novo
# elemento no fim da lista.
'''
a = input('')
lst.append(a)
'''
# e) Imprima a lista com o novo elemento inserido usando a função imprime_lista(lista).
'''
a = input('')
lst.append(a)
imprime_lista(lst)
'''
# f) No programa principal, remova o elemento no índice 2 da lista (responda mentalmente: qual
# seria esse elemento?).
'''
lst.pop(2)
imprime_lista(lst)
'''
# g) Imprima novamente a lista usando a função imprime_lista(lista).
imprime_lista(lst)

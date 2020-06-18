# Escreva um algoritmo (pode ser em fluxograma ou em Python) com uma função que recebe por parâmetro um
# vetor com uma quantidade qualquer de números inteiros e retorna um vetor idêntico ao recebido, a menos do
# primeiro e último valores, que trocarão de posição.
# Exemplo: Se o vetor recebido for | 2 | 6 | 4 | 1 | 9 | então o vetor de saída será | 9 | 6 | 4 | 1 | 2 |.

# função inverte primeiro e ultimo item da lista
def inverte_indice(vetor): #função para inverter primeiro e ultimo item da lista
    primeiro_da_lista = vetor.pop(0) #remove o primeiro da lista e atribui a var
    ultimo_da_lista = vetor.pop() #remove o ultimo da lista e atribui a var
    vetor.append(primeiro_da_lista) #adiciona o primeiro item removido a ultimo da lista
    vetor.insert(0, ultimo_da_lista ) #adiciona ultimo vetor a primeira posição da lista
    return vetor


#vetor = [2, 6, 4, 1, 9] #vetor do exemplo
#vetor = [1, 2, 3, 4, 5] #vetor de teste para inversão
vetor = ['a', 'b', 'c', 'd', 'e'] #vetor de teste para inversão
#vetor = [False, True, False, True] #vetor de teste para inversão


lista = inverte_indice(vetor)
print(f'O vetor com o primeiro e ultimo itens com posição invertida é: {lista}')

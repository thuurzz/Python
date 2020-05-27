# função inverte primeiro e ultimo item da lista
def inverte_indice(vetor): #função para inverter primeiro e ultimo item da lista
   ult = len(vetor) - 1
   primeiro_da_lista = vetor[0] #remove o primeiro da lista e atribui a var
   ultimo_da_lista = vetor[ult] #remove o ultimo da lista e atribui a var
   vetor[ult] = primeiro_da_lista #adiciona o primeiro item removido a ultimo da lista
   vetor[0] = ultimo_da_lista #adiciona ultimo vetor a primeira posição da lista
   return vetor


#vetor = [2, 6, 4, 1, 9] #vetor do exemplo
#vetor = [1, 2, 3, 4, 5] #vetor de teste para inversão
vetor = ['a', 'b', 'c', 'd', 'e'] #vetor de teste para inversão
#vetor = [False, True, False, True] #vetor de teste para inversão


lista = inverte_indice(vetor)
print(f'O vetor com o primeiro e ultimo itens com posição invertida é: {lista}')

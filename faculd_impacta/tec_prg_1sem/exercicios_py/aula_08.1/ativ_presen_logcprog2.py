#Arthur Vincius Santos Silva RA:1903665
#Contador de ocorrências na lista
def contavalor(vetor, x): #define a função
    tam = (len(vetor)) #defina tamanho da lista
    conta = 0 #inicia o contador em 0
    for item in range(tam): #repete o bloco len(n) vezes
        if vetor[item] == x: #verifica se o x esta na lista a cada iteração
            conta += 1 #adiciona +1 caso tenha o x na lista
    return conta #retona função


lista = [] #inicia lista vazia
print('digite 5 valores para criar uma lista: ')
for i in range(5):
    n = int(input(f'digite o número da posição {i + 1}: ')) #pede valores 5x
    lista.append(n) #adiciona a lista

x = int(input('escolha um número para ser buscado na lista: ')) #pede o x para procurar

ocorrencias = contavalor(lista, x) #chama a função
print('') #pula linha
print(f'O número {x}, tem {ocorrencias} ocorrências na lista!') #imprime na tela

# URI Online Judge | 1260 
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1260

# pede a quantidade de testes 
qtdTestes = int(input())
input() 

for i in range(qtdTestes):
    listArv = []
    while True:
        if i + 1 == qtdTestes:
            # Coloca cada espécie de árvore na lista.
            try:
                arv = input()
                if arv == '':
                    break
                listArv.append(arv)
            except EOFError:
                break
        arv = input()
        if arv == '':
            break
        listArv.append(arv) 
        

    # Divide 100% na pela quantidade de itens na lista
    porct = 100 / len(listArv)
    
    # Transforma lista de arvores em set, para ordenar e tirar os repetidos.
    ordLarv = set(listArv) # Remove repetidos com set
    ordLarv = list(ordLarv) # Transforma set em lista
    ordLarv.sort() # Ordena lista
    listArv.sort()


    # Exibe cada item da lista sem repetir, multiplica a quantidade de entradas que encontra na lista, pela porcentagem encontrada de cada quantidade.
    # Começo da lista para verificar
    comeco = 0
    # Passeia pela lista ordenada sem repetidos
    for esp in ordLarv:
        # Acumulador de vezes que aparece na lista
        cont = 0
        # Passeia pela lista de repetidos ordenados
        for j in range(comeco, len(listArv), 1):
            # Se o item atual for igual ao da lista de repetidos cont += 1.
            if esp == listArv[j]:
                cont += 1
                # Indica começo da próxima verificação para diminuir busca
                comeco += 1
        # Exibe espécie atual e multiplica a quantidade de vezes que aparece pelo percentual.
        print(f'{esp} {cont * porct:.4f}')
        
    # Imprime linha vazia entre 2 casos de teste, nu ultimo não.
    if i+1 != qtdTestes:
        print()
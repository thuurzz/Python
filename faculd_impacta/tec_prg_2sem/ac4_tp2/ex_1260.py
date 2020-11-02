# URI Online Judge | 1260 
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1260

# pede a quantidade de testes 
qtdTestes = int(input())
input() 

for i in range(qtdTestes):
    listArv = []
    while True:
        if i+1 == qtdTestes:
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

    # Tranforma lista de arvores em set, para ordenar e tirar os repetidos.
    ordLarv = set(listArv) # Remove repetidos com set
    ordLarv = list(ordLarv) # Transforma set em lista
    ordLarv.sort() # Ordena lista

    # Exibe cada item da lista sem repetir, multiplica a quantidade de entradas que encontra na lista, pela porcentagem encontrada de cada quantidade.
    for j in ordLarv:
        print(f'{j} {listArv.count(j) * porct:.4f}')
    if i+1 != qtdTestes:
        print()

'''
2

Red Alder
Ash
Aspen
Basswood
Ash
Beech
Yellow Birch
Ash
Cherry
Cottonwood
Ash
Cypress
Red Elm
Gum
Hackberry
White Oak
Hickory
Pecan
Hard Maple
White Oak
Soft Maple
Red Oak
Red Oak
White Oak
Poplan
Sassafras
Sycamore
Black Walnut
Willow

Red Alder
Ash
'''
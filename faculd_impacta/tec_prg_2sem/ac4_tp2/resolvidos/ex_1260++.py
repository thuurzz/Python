# URI Online Judge | 1260 
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1260

# pede a quantidade de testes 
qtdTestes = int(input())
input()

for i in range(qtdTestes):
    dictArv = {}
    cont = 0
    while True:
        # Ultimo caso
        try:
            if i+1 == qtdTestes:
                # Coloca cada espécie de árvore na lista.
                especie = input()
                if especie == '':
                    break
                elif especie not in dictArv:
                    dictArv.update({especie: 1 })
                else:
                    dictArv[especie] += 1
                cont += 1
        except EOFError:
            break
        # Outros casos
        especie = input()
        if especie == '':
            break
        elif especie not in dictArv:
            dictArv.update({especie: 1 })
        elif especie in dictArv:
            dictArv[especie] += 1
        cont += 1

    # Divide 100% na pela quantidade de itens na lista
    porct = 100 / cont

    for j in sorted(dictArv):
        if j in dictArv:
            print(f'{j} {(dictArv[j] * porct):.4f}')

    # Imprime linha vazia entre 2 casos de teste, no ultimo não.
    if i+1 != qtdTestes:
        print()
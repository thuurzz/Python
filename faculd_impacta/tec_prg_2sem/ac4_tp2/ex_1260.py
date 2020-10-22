# URI Online Judge | 1260 

while True:

    q = input()
    if q == '':
        break
    qtde = int(q)

# pede a quantidade de testes     
for i in range(qtde):
    #enquanto a entrada for diferente de ' ', pede entrada.
    lArv=[]
    while True:
        arv = input()
        if arv == '':
            break
        lArv.append(arv)

    valor=[]
    calc=100/len(lArv)
    
    #transf lArv em set
    ordLarv = set(lArv)
    ordLarv = list(ordLarv)
    ordLarv.sort()
    
    for i in ordLarv:
       print(f'{i} {lArv.count(i) * calc:.4f}')

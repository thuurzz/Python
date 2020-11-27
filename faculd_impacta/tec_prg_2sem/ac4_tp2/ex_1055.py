# URI Online Judge | 1055
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1055

aux=[]
soma=[]
lista=[]

qtde=int(input())
for i in range(qtde):
    l=input().split()
    aux=[int(i)for i in l]
    aux.sort()
    print(aux)
    p=len(aux)//2
    c=True
    if(len(aux) %2==0):
        
        while aux!=[]:
            if(c==True):
                lista.insert(0,aux[len(aux)-1])
                lista.append(aux[0])
                del(aux[0])
                del(aux[len(aux)-1])
                c=False
            else:
                lista.insert(0,aux[0])
                lista.append(aux[len(aux)-1])
                del(aux[0])
                del(aux[len(aux)-1])
                c=True
    
    else:
         while aux!=[]:
            if(len(aux)==1):
                del(aux[0])
                break
            if(c==True):
                lista.insert(0,aux[len(aux)-1])
                lista.append(aux[0])
                del(aux[0])
                del(aux[len(aux)-1])
                c=False
            else:
                lista.insert(0,aux[0])
                lista.append(aux[len(aux)-1])
                del(aux[0])
                del(aux[len(aux)-1])
                c=True
    print(lista)
    
    somanumero=0
    for i in range(len(lista)-1):
        somanumero=somanumero+abs(lista[i]-lista[i+1])
    soma.append(somanumero)
    print(soma)
    
        
        
'''

Algoritmo guloso!
começa com uma lista b com a maior diferença e
vai acrescentando os números que têm a maior diferença!

por exemplo, uma lista de 10 números
a = [0 3 9 5 4 1 7 8 6 2]
10! permutações: 10*9*8*7...*2*1
ordena <<<< A chave é ordenar primeiro!!
a = [0 1 2 3 4 5 6 7 8 9]
b = []
enquanto a != []:
    tira menor e maior e coloca
    menor no começo e maior no final em outra lista:
    a = [1 2 3 4 5 6 7 8] e b = [0 9] [menor e maior]
    agora inverte:
    tira menor e maior e coloca
    MAIOR no começo e MENOR no final em outra lista:
    a = [2 3 4 5 6 7] e b = [8 0 9 1] [maior e menor]
.
.
.

em resumo:
a = [0 1 2 3 4 5 6 7 8 9] e b = []
a = [1 2 3 4 5 6 7 8] e b = [0 9] [menor e maior]
a = [2 3 4 5 6 7] e b = [8 0 9 1] [maior e menor]
a = [3 4 5 6] e b = [2 8 0 9 1 7] [menor e maior]
a = [4 5] e b = [6 2 8 0 9 1 7 3] [maior e menor]
a = [] e b = [4 6 2 8 0 9 1 7 3 5] [menor e maior]

Exemplo do programa:
a = [4 2 1 5]
ordena <<<< A chave é ordenar primeiro!!
a = [1 2 4 5]
b = []
enquanto a != []:
    tira menor e maior e coloca
    menor no começo e maior no final em outra lista:
    a = [2 4] e b = [1 5] [menor]b[maior]
    agora inverte:
    tira menor e maior e coloca
    MAIOR no começo e MENOR no final em outra lista:
    a = [] e b = [4 1 5 2] [maior]b[menor]

Obs
só que tem tomar cuidado quando len(a) é impar. aí não dá para
colocar dois valores em b no final. nesse caso, coloca na ponta
que dá a soma maior.

4 4 2 1 5
  4 
2 5 1 4 = 10
'''

        






    

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
    
        
        
         

        






    

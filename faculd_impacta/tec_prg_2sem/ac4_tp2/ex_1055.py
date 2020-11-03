# URI Online Judge | 1055
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1055

""" Thiago Souza Do Amparo - 1904089 """

def permutacao_elegante(Sequencia):

    Impar = False
    
    Lista = Sequencia
    Lista.sort()

    if (len(Lista) % 2) != 0:

        Impar = True
        NumeroCentral = Lista.pop(len(Lista)//2)

    Saida = []

    while Lista != []:

        Saida.insert(0, Lista.pop())
        Saida.append(Lista.pop(0))

        if Lista == []:

            break
        
        Saida.insert(0, Lista.pop(0))
        Saida.append(Lista.pop())

    if Impar:

        if len(Saida) <= 4:
            
            if Saida[0] > Saida[len(Lista)]:

                Saida.insert(0,NumeroCentral)        
                print(Saida)
            else:
                    
                Saida.append(NumeroCentral)
                print(Saida)

        else:            

            if Saida[0] + Saida[1] > Saida[len(Lista)] + Saida[len(Lista)-1]:

                Saida.insert(0,NumeroCentral)        

            else:
                    
                Saida.append(NumeroCentral)
                
    Maior = 0    
    Sub = 0
       
    for j in range(1,len(Saida)):

        if Saida[j-1] - Saida[j] < 0:
                
            Sub += (Saida[j-1] - Saida[j]) * -1
                
        else:
                
            Sub += Saida[j-1] - Saida[j]
                
    if Sub > Maior:
        
        Maior = Sub
            
    Sub = 0

    return Maior

Casos = int(input())

Cont = 1
while Cont <= Casos:

    Sequencia = [int(x) for x in input().split()]
    N = Sequencia.pop(0)

    Sequencia = Sequencia[:N]
    
    Saida = permutacao_elegante(Sequencia)

    print('Case {}: {}'.format(Cont,Saida))

    Cont += 1


    

'''
controles = {'D':+1,'E':-1 ,'F':[1,1]}

lado = {'N':[1],'S':[2],'L':[3],'O':[4]}

posMapa = [2,2]

robozinho = ['', [0,0]]

robozinho[1] + controles['F']

listaDeMov = ['D', 'E']

movimenta(listaDeMov):

0 0 0 
0 0 0
0 0 0


if estado == 'N':
    posMapa[0] += -1
'''

saida=True
while saida==True:

    nlinhas, mcolunas, instruções=input().split()
    estado=""
    pontos=0
    
    posicao=[]
    if nlinhas=="0" and mcolunas=="0" and instruções == "0":
        break
    #preencher a matriz 
    y=[[" "]*int(mcolunas)]* int(nlinhas)
    for i in range(int(nlinhas)):
        linha=""
        linha=list(input())
        #encontra a posição e a orientação do robô
        for j in range(len(linha)):
            if(linha[j]!="." and linha[j]!="*" and linha[j]!="#"):
                estado=linha[j]
                posicao=[i,j]
            y[i]=linha
        
                
            
        

    
    
   

    #recebe a string de ações
    acoes=list(input())
    #verifica a string de ações
    for k in range(len(acoes)):
        if(acoes[k]=="D"):
          
            if(estado=="N"):
                estado="L"
            elif(estado=="O"):
                estado="N"
            elif(estado=="S"):
                estado="O"
            elif(estado=="L"):
                estado="S"
        elif(acoes[k]=="E"):

            if(estado=="N"):
                estado="O"
            elif(estado=="O"):
                estado="S"
            elif(estado=="S"):
                estado="L"
            elif(estado=="L"):
                estado="N"
        
        
        #processo para executar a locomoção do robo
        elif(acoes[k]=="F"):
            
            if(estado=="N"):
                # ponto NORTE
                if(posicao[0]>0 and y[posicao[0]-1][posicao[1]]=="*" ):
                    pontos=pontos+1
                    y[posicao[0]-1][posicao[1]]=estado
                    y[posicao[0]][posicao[1]]="."
                    posicao=[posicao[0]-1,posicao[1]]

                elif(posicao[0]>0 and y[posicao[0]-1][posicao[1]]=="#"):
                     y[posicao[0]][posicao[1]]=estado


                elif(posicao[0]>0 and y[posicao[0]-1][posicao[1]]=="."):
                    y[posicao[0]-1][posicao[1]]=estado
                    y[posicao[0]][posicao[1]]="."
                    posicao=[posicao[0]-1,posicao[1]]



            elif(estado=="S"):
                #pontos SUL
                if(posicao[0]!=(int(nlinhas)-1) and y[posicao[0]+1][posicao[1]]=="*"):
                    pontos=pontos+1
                    y[posicao[0]+1][posicao[1]]=estado
                    y[posicao[0]][posicao[1]]="."
                    posicao=[posicao[0]+1,posicao[1]]
                
                elif(posicao[0]!=(int(nlinhas)-1) and y[posicao[0]+1][posicao[1]]=="#"):
                     y[posicao[0]][posicao[1]]=estado
                
                elif(posicao[0]!=(int(nlinhas)-1) and y[posicao[0]+1][posicao[1]]=="."):
                    y[posicao[0]+1][posicao[1]]=estado
                    y[posicao[0]][posicao[1]]="."
                    posicao=[posicao[0]+1,posicao[1]]


                    
            elif(estado=="O"):
                #pontos OESTE
                if(posicao[1]>0 and y[posicao[0]][posicao[1]-1]=="*"):
                    pontos=pontos+1
                    y[posicao[0]][posicao[1]-1]=estado
                    y[posicao[0]][posicao[1]]="."
                    posicao=[posicao[0],posicao[1]-1]

                elif(posicao[1]>0 and y[posicao[0]][posicao[1]-1]=="#"):
                     y[posicao[0]][posicao[1]]=estado

                elif(posicao[1]>0 and y[posicao[0]][posicao[1]-1]=="."):
                    y[posicao[0]][posicao[1]-1]=estado
                    y[posicao[0]][posicao[1]]="."
                    posicao=[posicao[0],posicao[1]-1]

                
           
           
            elif(estado=="L"):
                #pontos LESTE
                if(posicao[1]!=(int(mcolunas)-1) and y[posicao[0]][posicao[1]+1]=="*"):
                    pontos=pontos+1
                    y[posicao[0]][posicao[1]+1]=estado
                    y[posicao[0]][posicao[1]]="."
                    posicao=[posicao[0],posicao[1]+1]
                
                elif(posicao[1]!=(int(mcolunas)-1) and y[posicao[0]][posicao[1]+1]=="#"):
                     y[posicao[0]][posicao[1]]=estado

                elif(posicao[1]!=(int(mcolunas)-1) and y[posicao[0]][posicao[1]+1]=="."):
                    y[posicao[0]][posicao[1]+1]=estado
                    y[posicao[0]][posicao[1]]="."
                    posicao=[posicao[0],posicao[1]+1]
                
                 





    print(pontos)
    
    
    
    

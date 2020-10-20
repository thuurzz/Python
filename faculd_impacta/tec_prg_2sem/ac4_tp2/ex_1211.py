# URI Online Judge | 1211

#lista exemplo dos telefones
listTel = [[535456], [535488], [536566], [835456]] 

#lê a lista com telefones
# (DESCOBRIR QUE PARADA É ESSA)A entrada é composta por diversas instâncias e termina com final de arquivo *(EOF)*.

#separa em lista com lista com números

# for com tamanho da lista com teste se o caracter do número de telefone da posição atual, está contido no próximo número de telefone.

# Caso contido, contador de caracter economizados, recebe +1.
carcEconm = 0

# Iterar lista de telefones, checando o atual com o próximo.
for tel in range(len(listTel)): #para cada tel na lista
    #prefixo pelo google, são 4 primeiros dígitos do tel
    prefixo = 4
    for caracter in range(prefixo): #para cada caracter do tel
        if caracter in listTel[tel +1]: # checa com os do tel seguinte
            carcEconm += 1 #caso já tenha, +1 no contador 


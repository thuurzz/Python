arq = open('compras.txt', 'w')                  #abre sobreescrevendo ou cria um aqruivo .txt
item = input('nome do item: ')                  #var que ira receber dado para ser escrito no txt
qtd = int(input('quantidade: '))                #var que ira receber dado para ser escrito no txt
arq.write(f'item: {item} | quantidade: {qtd}')  #função write escreve dentro do arquivo, assim como print faria na tela
arq.close()                                     #fecha o arquivo, finalizando a ação e forçando o buffer a escrever os dados no arquvo

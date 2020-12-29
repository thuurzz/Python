from functions import *
from interface import *

usuarios = {}

lOpt = ['Inserir', 'Pesquisar', 'Excluir', 'Listar','Sair']
while True:
    opt = menu(lOpt)
    if opt == 1:
        inserir(usuarios)
    elif opt == 2:
        chave = input('Qual a chave do que deseja pesquisar? ').strip().upper()
        pesquisar(usuarios, chave)
    elif opt == 3:
        chave = input('Qual a chave do que deseja excluir? ').strip().upper()
        excluir(usuarios, chave)
    elif opt == 4:
        listar(usuarios)
    elif opt == 5:
        titulo('FIM DO PROGRAMA')
        break


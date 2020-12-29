from interface import *

def inserir(dict):
    import random
    titulo('INSERIR USUÁRIO')
    chave = random.randint(10000000, 99999999)
    dict[chave] = [input('Digite o nome: ').strip().upper(),
                   input('Digite o login: ').strip().upper(),
                   input('Nível de usuário: [USR][ADM][GUEST] ').strip().upper(),
                   input('Digite a ultima hora de acesso: example(mm:hh) ').strip().upper(),
                   input('Digite a ultima data de acesso: example(DD/MM/AAA) ').strip().upper(),
                   input('Qual a ultima estação acessada: ').strip().upper()]
    linha()
    

def pesquisar(dict, chave):
    titulo('PESQUISA DE ITEM')
    for id, usr in dict.items():
        if usr[1] ==  chave:
            print('ID de sessão...: ' + str(id))
            print("Nome...........: " + usr[0])
            print("Login..........: " + usr[1])
            print("Nv de usuário..: " + usr[2])
            print("Último acesso..: " + usr[3])
            print("Último acesso..: " + usr[4])
            print("Última estação.: " + usr[5])
            print()
    linha()


def excluir(dicionario, chave):
    titulo('EXCLUIR ITEM')
    if dicionario.get(chave) != None:
        del dicionario[chave]
    print("Objeto Eliminado")
    linha()


def listar(dicionario):
    titulo('CADASTRO')
    for chave, valor in dicionario.items():
        print("Objeto......")
        print("ID de acesso: ", chave)
        print("Dados: ", ', '.join(valor))
        print()
    linha()
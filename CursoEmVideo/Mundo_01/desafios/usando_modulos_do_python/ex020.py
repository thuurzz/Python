import random
n1 = input('Digite o nome do aluno:')
n2 = input('Digite o nome do aluno:')
n3 = input('Digite o nome do aluno:')
n4 = input('Digite o nome do aluno:')

lista = [n1,n2,n3,n4]

random.shuffle(lista)

print('a ordem de apresentação será:')
print(lista)

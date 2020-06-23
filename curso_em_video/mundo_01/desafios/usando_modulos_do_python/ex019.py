# Um professor quer escolhar uma de duas aluna para apagar a lousa.
# Escreva um programa que gere um número aleatório que corresponda
# ao sorterio de uma das alunas para executar a tarefa!

import random

a = random.randint(1,4)

a1 = input('digite seu nome: ')
a2 = input('digite seu nome: ')
a3 = input('digite seu nome: ')
a4 = input('digite seu nome: ')

if a == 1:
    print('O aluno(a) escolhido foi:',a1)
elif a == 2:
    print('O aluno(a) escolhido foi:',a2)
elif a == 3:
    print('O aluno(a) escolhido foi:',a3)
else:
    print('O aluno(a) escolhido foi:',a4)

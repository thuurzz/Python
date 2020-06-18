# Um professor quer escolhar uma de duas aluna para apagar a lousa.
# Escreva um programa que gere um número aleatório que corresponda
# ao sorterio de uma das alunas para executar a tarefa!

import random

a = random.randint(1,4)

if a == 1:
    print('Mia Kalifah')
elif a == 2:
    print('Vivi Fernandes')
elif a == 3:
    print('Monica Mattos')
else:
    print('Lisa Ann')

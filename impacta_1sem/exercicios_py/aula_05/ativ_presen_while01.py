#Arthur Vinicius Santo Silva RA:19033665
'''
Crie um programa em Python que leia dois números inteiros num1 e num2 e efetue a
multiplicação usando somas sucessivas (use uma estrutura de repetição). Ao final, exiba o valor
da multiplicação entre num1 e num2.
'''
n1 = int(input())
n2 = int(input())
total = 0
i = n2

while i > 0:
    total = total + n1
    i = i - 1

print(total)





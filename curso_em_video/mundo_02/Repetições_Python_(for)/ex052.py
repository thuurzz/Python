# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número para verificar se este é primo: '))

# número primo deve ser divisível por 1 e por ele mesmo
div = 0
for i in range(1, n+1):
    if n % i == 0:
        div += 1
if div == 2:
    print('Este número é primo.')
else:
    print('Este número NÃO é primo.')

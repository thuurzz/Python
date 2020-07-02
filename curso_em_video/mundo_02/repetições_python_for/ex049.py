# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um
# número que o usuário escolher,
# só que agora utilizando um laço for.

'''
n = int(input('digite um número para exibir sua tabuada:'))
print('{} x 1 = {}'.format(n, (n * 1)))
print('{} x 2 = {}'.format(n, (n * 2)))
print('{} x 3 = {}'.format(n, (n * 3)))
print('{} x 4 = {}'.format(n, (n * 4)))
print('{} x 5 = {}'.format(n, (n * 5)))
print('{} x 6 = {}'.format(n, (n * 6)))
print('{} x 7 = {}'.format(n, (n * 7)))
print('{} x 8 = {}'.format(n, (n * 8)))
print('{} x 9 = {}'.format(n, (n * 9)))
print('{} x10 = {}'.format(n, (n * 10)))

'''

n = int(input('Digite um número para exibir sua tabuada: '))
for i in range(1, 11, 1):
    total = n * i
    print(f'{n} x {i} = {total}')
    print(15 * '=')

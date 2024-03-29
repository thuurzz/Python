# Exercício Python 35: Desenvolva um programa que leia o comprimento de três
# retas e diga ao usuário se elas podem ou não formar um triângulo.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

print('Digite os valores de 3 retas e sera calculado se estas podem formar um triângulo.')
a = float(input('valor a: '))
b = float(input('valor b: '))
c = float(input('valor c: '))

c1 = (b - c) < a < (b + c)
c2 = (a - c) < b < (a + c)
c3 = (a - b) < c < (a + b)

if c1 and c2 and c3:
    print('Estes valores podem formar um triângulo.')
    if a == b == c:
        print('Triângulo Esquilátero!')
    elif a == b or a == c:
        print('Triângulo Isóceles')
    else:
        print('Triângulo Escaleno')
else:
    print('Estes valores não podem formar um triângulo.')
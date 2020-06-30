# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag).

n = int(input('Digite um número: '))
soma = 0
cont = 0
while n != 999:
    if n != 999:
        soma += n
        cont += 1
        n = int(input('Digite um número: '))
print(f'Foram digitados {cont} números e a soma deles é: {soma}')
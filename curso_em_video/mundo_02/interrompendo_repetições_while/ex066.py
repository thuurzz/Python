# Exercício Python 66: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag). Use *break*


soma = cont = 0
while True:
    n = int(input('Digite um número: '))
    if n != 999:
        soma += n
        cont += 1
    else:
        break
print(f'Foram digitados {cont} números e a soma deles é: {soma}')
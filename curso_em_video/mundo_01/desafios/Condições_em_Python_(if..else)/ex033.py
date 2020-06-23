# Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print('Digite 3 números e o maior deles sera exibido. ')
n1 = int(input('primeiro número:'))
n2 = int(input('segundo número:'))
n3 = int(input('terceiro número:'))

maior = n1
if n2 > maior:
    maior = n2
    if n3 > maior:
        maior = n3
elif n3 > maior:
    maior = n3

menor = n1
if n2 < n1:
    menor = n2
    if n3 < n2:
        menor = n3
elif n3 < menor:
    menor = n3

print(f'O maior deles é {maior} e o menor {menor}')
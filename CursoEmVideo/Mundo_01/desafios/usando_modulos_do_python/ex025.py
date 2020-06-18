# Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = input('Digite seu nome completo: ').strip()
tem = 'silva' in nome.lower()

if tem:
    print('Seu nome tem Silva!')
else:
    print('Seu nome não tem Silva!')
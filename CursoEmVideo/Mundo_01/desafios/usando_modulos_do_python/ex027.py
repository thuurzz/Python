# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa
# mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Digite seu nome completo: ').strip()

nome_sep = nome.split()
print(f'Seu nome e sobrenome são: {nome_sep[0]} {nome_sep[-1]}')

#Arthur Vincius Santos Silva
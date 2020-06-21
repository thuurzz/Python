# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

print('Digite um número inteiro e este sera convertido para a opção escolhida: ')
print('=' * 80)
print('''[1] Binário 
[2] Octal 
[3]Hexadecimal''')

number = int(input('Digite o número para conversão: '))
opcao = int(input('Escolha a opção de conversão: '))

# lstrip helps remove "0x" from the left
# rstrip helps remove "L" from the right,
# L represents a long number


def conv_bin(number):
    n_bin = bin(number).lstrip("0b").rstrip("L")
    print(f'O número {number} em binário é: {n_bin}')


def conv_octal(number):
    n_oct = oct(number).lstrip("0o").rstrip("L")
    print(f'O número {number} em octal é: {n_oct}')


def conv_hexa(number):
    n_hex = hex(number).lstrip("0x").rstrip("L")
    print(f'O número {number} em hexa é: {n_hex}')


# [1] Binário [2] Octal [3]Hexadecimal
if opcao == 1:
    conv_bin(number)
elif opcao == 2:
    conv_octal(number)
else:
    conv_hexa(number)

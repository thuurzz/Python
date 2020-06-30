"""
 Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

print('Digite dois valores, depois selecione a opção desejada.')
n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))

opc = 0
while not opc == 5:
    opc = int(input('''Digite a operação desejada:
[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa
====================
'''))
    if opc == 1:
        soma = n1 + n2
        print(f'\033[7mA soma dos valores é: {soma}\033[m')
        print('=' * 30)

    elif opc == 2:
        mult = n1 * n2
        print(f'\033[7mA multiplicação dos valores é: {mult}\033[m')
        print('=' * 30)

    elif opc == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print(f'\033[7mO maior destes 2 números é: {maior}\033[m')
        print('=' * 30)

    elif opc == 4:
        n1 = int(input('Digite o 1º valor: '))
        n2 = int(input('Digite o 2º valor: '))
        print('=' * 30)
        print(f'\033[7mOs novos valores são: {n1} e {n2}.\033[m')
    else:
        print('\033[7m=\033[m' * 40)
        print('Progrma finalizado, volte sempre!')

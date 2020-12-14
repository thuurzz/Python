# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def calcArea(largura, comprimento):
    print('=' * 30)
    print(f'{"CALCULO DE ÁREA":^30}')
    print('=' * 30)

    area = largura * comprimento
    print(f'A área do terreno de largura {largura} e comprimento {comprimento} é: {area:.2f} m2.')

    print('=' * 30)
    print(f'{"FIM DO PROGRAMA":^30}')
    print('=' * 30)


l = float(input('Digite a largura do terreno em metros: '))
c = float(input('Digite o comprimento do terreno em metros: '))

calcArea(c,l)
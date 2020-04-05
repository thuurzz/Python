#Escreva um programa que lê dois valores inteiros e exibe o resultado do primeiro número
#dividido pelo segundo número, com exatamente duas casas decimais.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

div = (n1 / n2)

print('A divisão do primeiro número pelo segundo é: {:.02f}'.format(div))

#Escreva um programa que lê dois valores em ponto flutuante e exibe o resultado do primeiro
#dividido pelo segundo, com exatamente seis dígitos depois da vírgula.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

div = (n1 / n2)

print('A divisão do primeiro número pelo segundo é: {:.07f}'.format(div))

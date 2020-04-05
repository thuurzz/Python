#Escreva um programa que receba três números quaisquer e apresente:
#a) a soma dos quadrados dos três números;
#b) o quadrado da soma dos três números.

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

s_qdr = n1**2 + n2**2 + n3**2

qdr_s = (n1 + n2 + n3) ** 2

print('A soma dos quadrados dos três números é: {} \nO quadrado da soma dos três números é: {}'.format(s_qdr, qdr_s))

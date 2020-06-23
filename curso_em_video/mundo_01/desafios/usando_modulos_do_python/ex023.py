#Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

n = int(input('Digite um número  de 0 a 9999: '))
while (n < 0) or (n > 9999):
    n = int(input ('O número deve estar entre 0 e 9999:'))
    

n = str(n)

i = 0
j = 1
while j < 5:  
    print(n[i:j])
    i += 1
    j += 1



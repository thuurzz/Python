#Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

n = int(input('Digite um número  de 0 a 9999: '))
while (n < 0) or (n > 9999):
    n = int(input ('O número deve estar entre 0 e 9999:'))
    
milhar = n // 1000
n = n - (milhar * 1000) 
centena = n // 100
n = n - (centena * 100)
dezena = n // 10
n = n - (dezena * 10)
unidade = n // 1

print(milhar)
print(centena)
print(dezena)
print(unidade)
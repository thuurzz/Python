# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. 
# No final, mostre qual foi o maior e o menor peso lidos.
import sys
pesado = 0
leve = sys.maxsize

for i in range(5):
    peso = int(input('Digite seu peso: '))
    if peso > pesado:
        pesado = peso
    if peso < leve:
        leve = peso
        
print(f'O maior peso foi: {pesado}')
print(f'O menor peso foi: {leve}')


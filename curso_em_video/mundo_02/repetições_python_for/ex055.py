# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. 
# No final, mostre qual foi o maior e o menor peso lidos.
pesado = 0
leve = 0

for posicao in range(5):
    peso = int(input(f'Digite seu peso da {posicao + 1}º pessoa: '))
    if posicao == 1:
        pesado = peso
        leve = peso
    else:
        if peso > pesado:
            pesado = peso
        if peso < leve:
            leve = peso
        
print(f'O maior peso foi: {pesado}kg.')
print(f'O menor peso foi: {leve}kg.')


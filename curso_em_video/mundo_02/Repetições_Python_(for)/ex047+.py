 # Exercício Python 47: Crie um programa que mostre na tela todos os
 # números pares que estão no intervalo entre 1 e 50.

pares_1_50 = []
for i in range(2, 50+1, 2):
    pares_1_50.append(i)

print(f'Os pares de 1 até 50 são: {pares_1_50}')

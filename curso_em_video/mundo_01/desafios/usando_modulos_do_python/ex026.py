# Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input('Digite uma frase: ').strip()

pos = []
for i in range(len(frase)):
    if 'A' == frase.upper()[i]:
        pos.append(i)


print(f'A letra "A" aparece {len(pos)} vez(es) pela primeira na posição {pos[0]+1} e por ultimo na posição {pos[-1]+1}. ')

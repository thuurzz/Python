# Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input('Digite uma frase: ').strip().upper()

print(f'A letra "A" aparece {frase.count("A")} vez(es) na frase.')
print(f'A primeira ocorrência da letra "A" na frase é na posição: {frase.find("A")+1}')
print(f'A ultima ocorrência da letra "A" na frase é na posição: {frase.rfind("A")+1}')
# Exercício Python 50: Desenvolva um programa que leia seis números
# inteiros e mostre a soma apenas daqueles
# que forem pares. Se o valor digitado for ímpar, desconsidere-o.

print('Digite uma sequência de 6 número inteiros e sera exibida a soma dos pares digitados.')
total = 0
for i in range(6):
    n = int(input(f'Digite o {i + 1}º número: '))
    if n % 2 == 0:
        total += n

print(f'O total da soma dos pares da sequência digitada é: {total}')

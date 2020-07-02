# Exercício Python 48: Faça um programa que calcule a soma entre todos os
# números que são múltiplos de três e que se
# encontram no intervalo de 1 até 500.

total = 0
div_3 = []
for i in range(1, 501, 2):
    if i % 3 == 0:
        div_3.append(i)
        total += i

print(f'A soma dos divisíveis por 3 de 1 até 500 é: {total}')
print(div_3)

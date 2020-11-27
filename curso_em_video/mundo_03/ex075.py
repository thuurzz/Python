# ex075

tupN = (int(input('Digite um número: ')), 
        int(input('Digite o segundo número: ')), 
        int(input('Digite o terceiro número: ')), 
        int(input('Digite o quarto número: ')))

print()
print(f"A lista de números é: {tupN}")
# Quantas vezes apareceu o número 9?
print(f'O número 9 apareceu: {tupN.count(9)} vezes.')
print('=' * 20)
# Em que posição foi digitado o primeiro valor 3.\
try:
    print(f'O valor 3 apareceu a primeira vez na posição: {tupN.index(3)+1}.')
except ValueError:
    print('O valor 3 não consta na lista!')
print('=' * 20)
# Quais foram os números pares.
for n in tupN:
    if n % 2 == 0:
        print(f'Dentro da lista conta o valor par: {n}')
print('=' * 20)
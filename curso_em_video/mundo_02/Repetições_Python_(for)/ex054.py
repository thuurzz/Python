# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

menor = maior = 0
for i in range(7):
    idade = int(input(' Digite sua idade: '))
    if idade < 18:
        menor += 1
    elif idade >= 18:
        maior += 1
        
print(f'Das sete idades digitadas, {menor} são menores e {maior} são maiores de idade.')

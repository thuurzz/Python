# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

ano_atual = date.today().year
maior = menor = 0

for i in range(7):
    nasc = int(input(' Digite sua data de nascimento: '))
    idade = ano_atual - nasc
    if idade < 21:
        menor += 1
    elif idade >= 21:
        maior += 1
        
print(f'Das sete idades digitadas, {menor} são menores e {maior} são maiores de idade.')

# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

print('Digite o valor do seu salário, para valores acima R$1250.00 acréscimo de 10%, abaixo desse valor acrescimo de 15%.')

salario = float(input('Qual valor do seu salário: '))

if salario <= 1250:
    salario *= 115/100
else:
    salario *= 110/100

print(f'O valor com aumento é de: R${salario:.2f}')

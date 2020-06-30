# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

n = int(input('Digite um número para exibir seu fatorial: '))  # pede o número
cont = n  # var contadora
fat = 1
print(f'Calculando {n}!')
while cont > 0:  # vai de 1 até o número fatorial
    print(f'{cont} x {fat}')
    fat *= cont  # multiplica primeiro por 1 depois atualiza o fat com a próx multiplicação
    cont -= 1  # adicona 1 ao contador
    print(f'Total = {fat}')

fatf = 1
for i in range(1, n + 1):
    fatf *= i

print(f'O valor do fatorial de {n} é: {fat} #com while')  # exibe resultados
print(f'O valor do fatorial de {n} é: {fatf} #com for')  # exibe resultados

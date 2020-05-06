# Lucas da Silva Santos RA: 1904209
# Arthur Vinicius Santos Silva RA: 1903665
# Brasilio Soares de Campos Neto RA: 1902861

def calc_fat(n):
    fator = 1
    cont = 1

    while (cont <= n):
        fator = (fator * cont)
        cont = cont + 1
    return (fator)


while True:
    n = int(input('Digite um numero impar: '))
    if n % 2 == 0:
        print('Numero invalido, tente novamente:')
    else:
        break


i = 1
soma = 0
while i <= n:
    soma += calc_fat(i)
    i += 2

print('A soma dos fatoriais ate o numero {}, e: {}'.format(n, soma))




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


def pede_impar():
    while True:
        n = int(input('Digite um numero impar: '))
        if n % 2 == 0 and n != 1:
            print('Numero invalido, tente nomanente:')
        else:
            break
    return n


def soma_fat_impar(n):
    i = 1
    soma = 0
    while i <= n:
        soma += calc_fat(i)
        i += 2

    return soma


a = soma_fat_impar(pede_impar())
print('O valor da soma dos fatoriais impares ate o numero digitado, resulta em: {}'.format(a))



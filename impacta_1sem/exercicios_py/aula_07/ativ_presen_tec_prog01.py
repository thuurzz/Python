#Arthur Vinicius Santos Silva RA:1903665
print('Digite um número de 0 a 9, após escolha: 1-Tabuada de Adição e 2-Tabuada de Multiplicação.')

def tabuada(n, modo):
    if (modo == 1):
        for i in range(0, 10+1, 1):
            print('{} + {} = {}'.format(i, n, (i + n)))
    elif(modo == 2):
        for i in range(0, 10+1, 1):
            print('{} * {} = {}'.format(i, n, (i * n)))
    else:
        print('modo inválido! Escolha 1 ou 2')


n = int(input('Número: '))
modo = int(input('[1]Tabuada de Adição \n[2]Tabuada de Multiplicação.\n'))

tabuada(n, modo)

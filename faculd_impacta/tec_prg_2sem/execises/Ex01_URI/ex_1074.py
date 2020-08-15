# URI Online Judge | 1074

# Leia um valor inteiro N.
x = int(input())

par = impar = positivo = negativo = 0

for i in range(x):
    status = []
    n = int(input())
    if n == 0:
        status.append('NULL')
    else:
        # verifica se par ou impar
        if n % 2 == 0:
            status.append('EVEN')
        else:
            status.append('ODD')
        # verfica se positivo ou negativo
        if n > 0:
            status.append('POSITIVE')
        elif n < 0:
            status.append('NEGATIVE')
    status = ' '.join(status)
    print(f'{status}')

print('Olá, escolha dois números:')
n1 = float(input('digite o primeiro número:'))
n2 = float(input('digite o segundo número:'))

print('os números escolhidos foram {} e {}'.format(n1, n2))

ponte = n1
n1 = n2
n2 = ponte

print('os números escolhidos em ordem contrária são: {} e {}'.format(n1, n2))

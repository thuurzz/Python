# recebe número para exibir tabuada
n = int(input('Digite um número para exibir sua tabuada, para terminar, digite um número negativo. '))

# laço infito, até digitar negativo
while n >= 0:
    if n >= 0:  # se n positivo, exibe tabuada de n
        print('=' * 20)
        for numero in range(1, 11):
            total = numero * n
            print(f'{numero} x {n} = {total}')
        print('=' * 20)
        n = int(input('Digite um número para exibir sua tabuada, para terminar, digite um número negativo. '))
    else:
        break
print('FIM!')

#EX081

lNum = []
while True:
    n = int(input('Digite um valor: '))
    lNum.append(n)
    opc = input('Deseja continuar? [S/N]').lower()
    while opc not in 'sn':
        opc = input('Deseja continuar?[S/N]').lower()[0]
    if opc == 'n':
        break

# Mostre quantos números foram digitados\
print(f'Foram digitados {len(lNum)} números.')

# A lista de valores ordenada de forma decrescente
lNum.sort(reverse=True)
print(f'A lista de valores ordenada de forma decrescente é:{lNum}')

# Se o valor 5 foi digitado e está ou não na lista
if 5 in lNum:
    print(f'O valor 5 foi encontrado na lista.')
else:
    print(f'O valor 5 não consta na lista.')
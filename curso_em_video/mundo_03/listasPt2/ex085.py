#EX085

# Define listas vazias
num = [[],[]]

# Pede 7 números
for i in range(1,7+1):
    n = int(input(f'Digite o {i}* valor:'))
    # Separa em lista de pares e impares
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)

# Exibe valores
num[0].sort()
print(f'Os valores pares digitados foram: {num[0]}')
num[1].sort()
print(f'Os valores impares digitados foram: {num[1]}')
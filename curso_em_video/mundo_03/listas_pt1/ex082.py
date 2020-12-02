#EX082

lNum = []
while True:
    n = int(input('Digite um valor: '))
    lNum.append(n)
    opc = input('Deseja continuar? [S/N]').lower()
    while opc not in 'sn':
        opc = input('Deseja continuar?[S/N]').lower()[0]
    if opc == 'n':
        break

# Cria lista apenas com valores pares e impares
lNumPares = []
lNumImpares = []
for num in lNum:
    if num % 2 == 0:
        lNumPares.append(num)
    else:
        lNumImpares.append(num)

# Exibe as 3 listas
# Interira
print(f'A lista de valores inteira é: {lNum}')
# Pares
print(f'A lista de valores pares é: {lNumPares}')
# Impares
print(f'A lista de valores impares é: {lNumImpares}')
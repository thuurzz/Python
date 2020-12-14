#EX087

# Criar matriz 3x3
matriz = []
for i in range(3):
    matriz.append([0,0,0])

# Preencher matriz 3x3
for i in range(3):
    for j in range(3):
        n = int(input(f'Digite o valor da posição: [{i}][{j}]: '))
        matriz[i][j] = n
       
# Exibir matriz 
for linha in matriz:
    print(linha)

# Soma de todos os valores pares
somaPares = 0
for linha in matriz:
    for num in linha:
        if num % 2 == 0:
            somaPares += num
print(f'A soma de todos os valores pares é : {somaPares}')

# A soma dos valores da terceira coluna
soma3Col = 0
for i in range(len(matriz)):
        soma3Col += matriz[i][2]
print(f'A soma dos valores da terceira coluna é : {soma3Col}')

# O maior valor da segunda linha
print(f'O Maior valor da segunda linha é: {max(matriz[1])}')

#EX086

# Criar matriz 3x3
matriz = []
for i in range(3):
    matriz.append([0,0,0])

# Preencher matriz 3x3
for l in range(3):
    for c in range(3):
        n = int(input(f'Digite o valor da posição: [{l}][{c}]: '))
        matriz[l][c] = n
       
# Exibir matriz 
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
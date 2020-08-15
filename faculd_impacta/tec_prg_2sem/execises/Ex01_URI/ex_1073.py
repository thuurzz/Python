# URI 1073

# Leia um valor inteiro N.
n = int(input())

# Apresente o quadrado de cada um dos valores pares, de 1 até N, inclusive N, se for o caso.
for i in range(1, n+2):
    if i % 2 == 0:
        print(f'{i}^{2} = {i**2}')
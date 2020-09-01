# URI Online Judge | 1078

# Leia 1 valor inteiro N (2 < N < 1000). A seguir, mostre a tabuada de N:      
# 1 x N = N      2 x N = 2N        ...       10 x N = 10N

# Lê inteiro para exibir tabuada
n = int(input())

# inicia total em 0
total = 0 
# loop de 1 a 10 (10+1)
for i in range(1,11):
    # multiplica n(entrada) por i(contador do loop)
    total = n * i
    # exibe resultadp
    print(f'{i} x {n} = {total}')
    
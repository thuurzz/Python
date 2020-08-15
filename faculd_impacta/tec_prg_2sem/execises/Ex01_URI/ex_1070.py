#URI 1070

# lê entrada inteira positiva
x = int(input())

# Em seguida apresente os 6 valores ímpares consecutivos a partir de X,
# um valor por linha, inclusive o X ser for o caso.
for i in range(6):
    # verifica se impar, se impar, mostra e soma 2.
    if not x % 2 == 0:
        print(x)
        x += 2
        # se par, soma 1, mostra.
    else:
        x += 1
        print(x) 
        x += 2
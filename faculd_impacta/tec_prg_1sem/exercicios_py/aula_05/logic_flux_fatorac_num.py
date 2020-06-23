def fator (n):
    fator = 1
    cont = 1

    while (cont <= n):
        fator = (fator * cont)
        cont = cont + 1
    print(fator)

n = int(input())

fator(n)

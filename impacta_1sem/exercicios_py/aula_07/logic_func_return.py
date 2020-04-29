def calcula_fator(n):
    fator = 1
    cont = 1

    while (cont <= n):
        fator = (fator * cont)
        cont = cont + 1
    return (fator)

soma = 0
impares = 1
i = 1


while i <= 20:
    print(impares)
    print(calcula_fator(impares))
    soma += calcula_fator(impares)
    i += 1
    impares += 2

print(soma)

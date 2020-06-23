def soma_algarismo(n):
    soma = 0

    while n > 0:
        a1 = n % 10
        soma += a1
        n = n // 10

    return soma


n = int(input())
total = soma_algarismo(n)
print(total)

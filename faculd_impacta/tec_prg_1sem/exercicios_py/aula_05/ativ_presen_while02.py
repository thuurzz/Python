#Arthur Vinicius Santo Silva RA:19033665

n = int(input('Digite um número: '))
s = 0 #acumuladora
i = 1 #contador
n1 = n


while i <= n:
    s = s + (i / n1)
    print(i, n1)
    i = i + 1
    n1 = n1 - 1


print(s)



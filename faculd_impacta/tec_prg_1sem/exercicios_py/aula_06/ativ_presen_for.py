#Arthur Vinicius Santo Silva RA:19033665

n = int(input('Digite um número: '))
s = 0 #acumuladora
n1 = n


for i in range(1, n + 1, 1):
    s = s + (i / n1)
    print(i, n1)
    n1 = n1 - 1


print(s)

# Arthur Vinicus Santos Silva RA:1903665

import math

a = float(input())  #lê em graus
rad = math.radians(a)  #converte radianos

n = int(input())  # lê o número de repetições
i = 0

while i <= n:
    sen = rad ** (i + 1) / math.factorial(i)

    cos = rad ** (i - 1) / math.factorial(i)

    i = i + 1

sen = round(sen, 5)
cos = round(cos, 5)

print(sen)
print(cos)

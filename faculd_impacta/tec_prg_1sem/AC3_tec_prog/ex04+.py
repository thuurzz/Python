# Arthur Vinicus Santos Silva RA:1903665

import math

a = float(input())  #lê em graus
n = int(input())  #lê o número de repetições
rad = math.radians(a) #transforma graus em radianos

i = 0
sen = 0
cos = 0
j = 1

while i <= n:
    sen += ((-1) ** i) * (rad ** (j)) / (math.factorial(j))
                #sinal        numerador       denominador

    cos += ((-1) ** i) * (rad ** (j - 1)) / (math.factorial(j - 1))

    i = i + 1
    j = j + 2

sen = round(sen, 5)
cos = round(cos, 5)

print(sen)
print(cos)

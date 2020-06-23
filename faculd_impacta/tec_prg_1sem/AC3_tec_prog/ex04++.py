# Arthur Vinicus Santos Silva RA:1903665

import math

a = float(input())  #lê em graus
n = int(input())  #lê o número de repetições
rad = math.radians(a) #transforma graus em radianos
seno = 0
cosseno = 0
i = 0


while i <= n:
    seno += math.pow(-1, i) * math.pow(rad, (2 * i + 1)) / math.factorial(2 * i + 1)
    cosseno += math.pow(-1, i) * math.pow(rad, (2 * i)) / math.factorial(2 * i)
    i = i + 1

seno = round(seno, 5)
cosseno = round(cosseno, 5)

print(seno)
print(cosseno)

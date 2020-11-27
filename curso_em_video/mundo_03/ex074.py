import random

""" JEITO 1
# Gera 5 números aleatórios
alea1 = random.randint(0,5)
alea2 = random.randint(0,5)
alea3 = random.randint(0,5)
alea4 = random.randint(0,5)
alea5 = random.randint(0,5)
# Cria lista de aletórios
tupAlea = alea1, alea2 ,alea3 ,alea4 ,alea5
print(tupAlea)
"""

# JEITO 2
# Gera 5 números aleatórios
tupAlea = tuple(str(random.randint(10000,99999)))

maior = menor = 0
for pos,num in enumerate(tupAlea):
    if pos == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

tupAlea = ' '.join(tupAlea)

print(f'''
A lista de aleatórios é: {tupAlea}
O menor desta lista é: {menor}
O maior desta lista é: {maior}
''')
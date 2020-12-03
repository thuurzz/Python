#EX088
import random
import time

# Apresentação
print(30 * '=')
print(f'{" PALPITES DA MEGA":.^30}')
print(30 * '=')

# Lista para todos os palpites
lPalpites = []

# Pergunta a quantidade de palpites
qtdPalpites = int(input('Quantos jogos devem ser sorteados? '))

# Gera sequência de palpites sem repetir números e coloca na lista
for i in range(qtdPalpites):
    palpites = []
    while len(palpites) < 6:
        num = random.randint(0, 60)
        if num not in palpites:
            palpites.append(num)
    palpites.sort()
    lPalpites.append(palpites)

for i in range(len(lPalpites)):
    print(f'Jogo {i+1}: {lPalpites[i]}')
    time.sleep(0.1)
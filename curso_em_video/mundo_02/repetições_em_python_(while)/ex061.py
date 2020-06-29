# Exercício Python 51: Desenvolva um programa que leia o
# primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
n = 10  # mostra os 10 primeiros elementos
ult = a1 + (n - 1) * r
ult += 1

print('=' * 30)
print('10 PRIMEIROS TERMOS DE UMA PA')
print('=' * 30)

# com for
'''
for i in range(a1, ult, r):
    print(i, end='=> ')
'''

# com while
i = 0
while i < n:
    an = a1 + (i * r)
    print(an, end='=> ')
    i += 1

print('FIM')

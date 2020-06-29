# Exercício Python 51: Desenvolva um programa que leia o
# primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ex062
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ex063

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
n = 10  # mostra os 10 primeiros elementos
ult = a1 + (n - 1) * r
ult += 1

print('=' * 30)
print('10 PRIMEIROS TERMOS DE UMA PA')
print('=' * 30)

# com while
i = 0
while i < n:
    an = a1 + (i * r)
    print(an)
    i += 1

# verifica se quer exxibir mais termos
mais_termos = 0
mais_termos = int(input('Gostaria de mostrar mais termos? Quantos? Se não, digite 0: '))
if mais_termos == 0:  # caso não queira, entra 0, encerra o programa
    print('FIM')
else:  # com mais termos
    a1 = an  # O primeiro termo passa a ser o ultimo da primeira PA
    n = mais_termos + 1  # lê a quantidade de termos, +1 para mostrar o 1º anterior e ultimo novo
    i = 0
    while i < n:
        an = a1 + (i * r)
        print(an, end='=> ')
        i += 1
    print('FIM')

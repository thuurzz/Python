# Exercício Python 51: Desenvolva um programa que leia o
# primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ex062
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ex063

primeiro = int(input('Digite o primeiro termo da PA: '))
termo = primeiro
razao = int(input('Digite a razão da PA: '))
total = 0
contador = 0
mais = 10

print('=' * 30)
print('10 PRIMEIROS TERMOS DE UMA PA')
print('=' * 30)

# caso não queira, entra 0, encerra o programa
while mais != 0:
    total = total + mais
    while contador < total:
        print(f'{termo} =>', end='')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Gostaria de mostrar mais termos? Quantos? Se não, digite 0: '))
print('FIM')



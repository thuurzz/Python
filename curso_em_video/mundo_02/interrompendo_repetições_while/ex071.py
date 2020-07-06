print('=' * 20)
print('****BANCO ITAUL****')
print('=' * 20)

# pede o valor do saque
saque = int(input('Digite o valor a ser sacado: R$ '))

# inicia a quantidade de notas
nota50 = nota20 = nota10 = nota1 = 0

# enquanto o valor é maior que o da nota, descresce do saque, soma 1 ao contador
while saque > 50:
    saque -= 50
    nota50 += 1
while saque >= 20:
    saque -= 20
    nota20 += 1
while saque >= 10:
    saque -= 10
    nota10 += 1
while saque >= 1:
    saque -= 1
    nota1 += 1

# se valor do contador maior que 0, mostra a quantidade de notas
if nota50 > 0:
    print(f'Total de {nota50} cedula(s) de R$50')
if nota20 > 0:
    print(f'Total de {nota20} cedula(s) de R$20')
if nota10 > 0:
    print(f'Total de {nota10} cedula(s) de R$10')
if nota1 > 0:
    print(f'Total de {nota1} cedula(s) de R$1')
    
print('=' * 20)
print('VOLTE SEMPRE!')
print('=' * 20)






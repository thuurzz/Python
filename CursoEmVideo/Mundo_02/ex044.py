valor = float(input('Digite o valor do produto: '))

avista = valor * 90/100
cartao = valor * 95/100
cartao2x = valor
cartao3x = valor * 120/100

pagamento = int(input('Digite a forma de pagamento:\n [1]À vista\n [2]Cartão\n [3]2x no cartão\n [4]3x ou mais\n'))
total = 0
if pagamento == 1:
    total = avista
elif pagamento == 2:
    total = cartao
elif pagamento == 3:
    total = cartao2x
elif pagamento == 4:
    total = cartao3x

print(f'O valor final do pagamento será: {total}')
print('olá, com base na quantidade de metros² de parede a ser coberta, calcularemos quantas latas de tinta e qual será seu custo.')

for

metros = float(input('digite a quantidade de metros² a serem cobertos:'))
lata_cobertura = (3*18)
lata_custo = 80

latas_preciso = round((metros/lata_cobertura) + 0.5)
#latas_preciso = round((metros/lata_cobertura))
latas_valor = float(latas_preciso * lata_custo)


print('serão necessárias {} lata(s) e estas custarão: {}'.format(latas_preciso, latas_valor))

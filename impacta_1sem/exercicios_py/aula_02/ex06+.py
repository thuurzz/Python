import math
print('olá, com base na quantidade de metros² de parede a ser coberta, calcularemos quantas latas de tinta e qual será seu custo.')

paredes = int(input('digite a quantidade de paredes a serem pintadas:'))
area = float(0)

for c in range(0, paredes):
    altura = float(input('digite a altura da parede:'))
    largura = float(input('digite a largura da parede:'))
    area = area + (altura*largura)


#print(area)
area_lata = float(18*3)
custo_lata = float(80)

qtd_lata = math.ceil((area/area_lata))

#print(qtd_lata)

custo_total = float(qtd_lata * custo_lata)


print('Teremos então {} m² de area a serem cobertas, serão necessárias {} lata(s) de tinta e esta(s) resulta(m) o valor total de: {}'.format(area, qtd_lata, custo_total))

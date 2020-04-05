#Calcule e apresente o volume de uma lata de óleo.
#v=π.r².altura

import math

diametro = float(input('Digite o valor do diâmetro da lata em m: '))
r = (diametro / 2)
alt = float(input('Digite a altura da lata em m: '))

v = (math.pi) * (r ** 2) * alt

print('O volume dessa lata é de: {:.02f}m³'.format(v))

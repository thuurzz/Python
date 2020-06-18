print('Digite a altura e largura de uma parede em metros e será calculada sua área e quantos litros de tinta serão necessários para pintar a parede:')
a = float(input('digite a altura da parede:'))
l = float(input('digite a largura da parede:'))
area = (a * l)
litros_tinta = (area / 2)

print('uma parede medindo {}m de altura e {}m de largura, tem área de {:.2f}m², neste caso serão utilizados {:.2f} litros de tinta.'.format(a, l, area, litros_tinta))

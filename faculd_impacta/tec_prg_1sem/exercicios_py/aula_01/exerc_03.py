import math

print('olá, digite o valor do raio de um circulo em milímetros e iremos calcular sua área!')

raio = float(input('valor do raio:'))
areaCirculo = round((raio**2)*math.pi,2)

print('com o valor do raio sendo:', raio, 'o valor da área sera:', areaCirculo, 'mm².')

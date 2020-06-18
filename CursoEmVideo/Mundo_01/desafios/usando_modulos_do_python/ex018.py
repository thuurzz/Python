import math

print('digite o valor de um ângulo em graus, será mostrado seu seno, cosse e tangente: ')

a = float(input('valor em graus: '))
rad = math.radians(a)

sen = round(math.sin(rad),2)
cos = round(math.cos(rad),2)
tg = round(math.tan(rad),2)

print('{} graus tem o valor de sen {}, cos {} e tg {}:'.format(a, sen, cos, tg))

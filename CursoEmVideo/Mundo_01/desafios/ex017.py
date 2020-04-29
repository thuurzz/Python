import math

print('digite os valores dos catetos do triângulo retanglo e será exibida a sua hipotenusa: ')

b = float(input('cateto b: '))
c = float(input('cateto c: '))

hip = math.hypot(b,c) #utilizando a lib math

'''
hip = math.pow(math.pow(b,2) + math.pow(c,2), 0.5) #sem lib math
'''

print(math.trunc(hip))

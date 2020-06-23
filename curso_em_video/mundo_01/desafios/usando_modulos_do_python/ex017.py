import math

print('digite os valores dos catetos do triângulo retanglo e será exibida a sua hipotenusa: ')

co = float(input('cateto oposto: '))
ca = float(input('cateto adjacente: '))
hip = math.hypot(co, ca) #utilizando a lib math

'''
hip = math.pow(math.pow(b,2) + math.pow(c,2), 0.5) #sem lib math
'''

hip = round(hip, 2)
print(f'O valor da hipotenusa é: {hip}')

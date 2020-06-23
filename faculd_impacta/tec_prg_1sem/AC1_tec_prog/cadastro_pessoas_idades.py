#Arthur Vinicius Santos Silva   RA:1903665

import math

nome1 = input()
idade1 = int(math.fabs(float(input()))//1)

nome2 = input()
idade2 = int(math.fabs(float(input()))//1)


nome3 = input()
idade3 = int(math.fabs(float(input()))//1)


nome4 = input()
idade4 = int(math.fabs(float(input()))//1)


nome5 = input()
idade5 = int(math.fabs(float(input()))//1)


print('Pessoa:', nome1, ',', idade1)

print('Pessoa:', nome2, ',', idade2)

print('Pessoa:', nome3, ',', idade3)

print('Pessoa:', nome4, ',', idade4)

print('Pessoa:', nome5, ',', idade5)


soma_idades = (idade1 + idade2 + idade3 + idade4 + idade5)

print(soma_idades)

media_arit = (idade1 + idade2 + idade3 + idade4 + idade5)/5

print(media_arit)

media_geom = int(( (idade1 * idade2 * idade3 * idade4 * idade5) ** (1/5) ) // 1)

print(media_geom)




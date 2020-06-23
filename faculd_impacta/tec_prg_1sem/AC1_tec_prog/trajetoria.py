#Arthur Vinicius Santos Silva   RA:1903665

import math

theta = float(input())

v = float(input())

g = float(input())

h = ((v ** 2) * ((math.sin(math.radians(theta))) ** 2)) / (2 * g)

print(h)

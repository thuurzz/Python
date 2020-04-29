import math

a = float(input())
n = int(input())
rad = math.radians(a)

i = 0
x = 1

while i <= n:
    sen += ((-1) ** i) * (rad ** (x)) / (math.factorial(x))

    cos += ((-1) ** i) * (rad ** (x - 1)) / (math.factorial(x - 1))

    i = i + 1
    x = x + 2

sen = round(sen, 5)
cos = round(cos, 5)

print(sen)
print(cos)

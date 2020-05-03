'''
maior = 0
n = 0
cond = True

while cond:
    n = int(input())
    if n > maior:
        maior = n

    if n >= 0:
        cond = True
    else:
        cond = False
        maior = 0

    print(maior)
'''

cond = True
n = int(input())
if n >= 0:
    menor_ = n
else:
    menor_ = 0

while cond:
    if n < menor_ and n > 0:
        menor_ = n

    if n >= 0:
        cond = True
    else:
        cond = False

    print(menor_)

    if n >=0:
        n = int(input())


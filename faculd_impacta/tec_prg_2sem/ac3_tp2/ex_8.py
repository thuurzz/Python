def f(x):
    print('Em f: x =', x)
    if x > 0:
        f(x - 1)

def g(y):
    if y > 0:
        g(y - 1)
    print('Em g: y =', y)

f(4)
g(5)

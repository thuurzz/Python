x = 1
def f(x):
    print('Em f: x =', x)
    x = 23

def g(x):
    print('Em g: x =', x)
    x = 87


print('1. x =', x)
f(41)
print('2. x =', x)
g(92)
print('3. x =', x)

# Veja o programa abaixo e diga qual a saída que ele irá apresentar. Execute o programa e verifique se sua previsão é correta.
# Veja o programa abaixo e diga qual a saída que ele irá apresentar. Execute o programa e verifique se sua previsão é correta.


def f(x):
    print('Em f: x =', x)
    if x > 0:
        g(x - 1)

def g(y):
    print('Em g: y =', y)
    if y > 0:
        f(y - 1)

f(7)

#f7
#g6
#f5
#g4
#f3
#g2
#f1
#f0
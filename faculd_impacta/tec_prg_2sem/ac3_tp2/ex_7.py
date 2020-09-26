# Veja o programa abaixo e diga qual a saída que ele irá apresentar. Execute o programa e verifique se sua previsão é correta.
def f(x):
    if x > 0:
        g(x - 1)
    print('Em f: x =', x)
    

def g(y):
    if y > 0:
        f(y - 1)
    print('Em g: y =', y)
    

f(8)


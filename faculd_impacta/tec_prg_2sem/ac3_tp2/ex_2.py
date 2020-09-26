# Veja o programa abaixo e diga qual a saída que ele irá apresentar. Execute o programa e verifique se sua previsão é correta.


def f1():
    print('Executando f1')
    f2()

def f2():
    print('Executando f2')
    f3()

def f3():
    print('Executando f3')

f1()

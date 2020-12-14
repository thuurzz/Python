# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num=1, show=False):
    """Recebe número e calcula fatorial, se pede para mostrar processo em show, exibe números e processo, se não apenas o resultado.

    Args:
        num (int, optional): [Valor para calcular fatorial]. Defaults to 1.
        show (bool, optional): [Mostra ou não processo dos valores do fatorial]. Defaults to False.

    Returns:
        [type]: [Retorna valor do fatorial.]
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(num=10, show=True))

    

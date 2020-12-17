"""Exercício Python 107: Crie um módulo chamado moeda que tenha as funções incorporadas aumentar(), diminuir()
, dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções. """


def aumentar(valor=0, taxa=0):
    """Recebe valor e retorna aumentando a porcentagem indicada.

    Args:
        valor (int, optional): [Valor para receber aumento]. Defaults to 0.
        taxa (int, optional): [Porcentagem de aumento]. Defaults to 1.

    Returns:
        [float]: [Valor com aumento]
    """
    taxa = taxa / 100
    res = valor + (valor * taxa)
    return res


def diminuir(valor=0, taxa=0):
    """Recebe valor e retorna diminuindo a porcentagem indicada.

    Args:
        valor (int, optional): [Valor para receber diminuir]. Defaults to 0.
        taxa (int, optional): [Porcentagem para  diminuir]. Defaults to 1.

    Returns:
        [float]: [Valor com decréscimo]
    """
    taxa = taxa / 100
    res = valor - (valor * taxa)
    return res


def dobro(valor=0):
    """[Retorna o dobro do valor recebido.]

    Args:
        valor (int, optional): [Valor para dobrar]. Defaults to 0.

    Returns:
        [float]: [Valor dobrado].
    """
    res = valor * 2
    return res


def metade(valor=0):
    """[Retorna a metade do valor recebido.]

    Args:
        valor (int, optional): [Valor para decrescer a metade]. Defaults to 0.

    Returns:
        [float]: [Retorna metade do valor.]
    """
    res = valor / 2
    return res

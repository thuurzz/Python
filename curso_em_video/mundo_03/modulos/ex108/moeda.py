'''
Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
'''


def aumentar(valor=0, taxa=0):
    """Recebe valor e retorna aumentando a porcentagem indicada.

    Args:
        valor (int, optional): [Valor para receber aumento]. Defaults to 0.
        qtd (int, optional): [Porcentagem de aumento]. Defaults to 1.

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
        qtd (int, optional): [Porcentagem para  diminuir]. Defaults to 1.

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


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')
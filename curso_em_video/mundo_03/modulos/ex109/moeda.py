'''
Exercício Python 109: Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
'''


def aumentar(valor=0, taxa=0, formatar=False):
    """Recebe valor e retorna aumentando a porcentagem indicada.

    Args:
        valor (int, optional): [Valor para receber aumento]. Defaults to 0.
        qtd (int, optional): [Porcentagem de aumento]. Defaults to 1.

    Returns:
        [float]: [Valor com aumento]
    """
    taxa = taxa / 100
    res = valor + (valor * taxa)
    return res if formatar is False else moeda(res)


def diminuir(valor=0, taxa=0, formatar=False):
    """Recebe valor e retorna diminuindo a porcentagem indicada.

    Args:
        valor (int, optional): [Valor para receber diminuir]. Defaults to 0.
        qtd (int, optional): [Porcentagem para  diminuir]. Defaults to 1.

    Returns:
        [float]: [Valor com decréscimo]
    """
    taxa = taxa / 100
    res = valor - (valor * taxa)
    return res if not formatar else moeda(res)


def dobro(valor=0, formatar=False):
    """[Retorna o dobro do valor recebido.]

    Args:
        valor (int, optional): [Valor para dobrar]. Defaults to 0.

    Returns:
        [float]: [Valor dobrado].
    """
    res = valor * 2
    return res if not formatar else moeda(res)

def metade(valor=0, formatar=False):
    """[Retorna a metade do valor recebido.]

    Args:
        valor (int, optional): [Valor para decrescer a metade]. Defaults to 0.

    Returns:
        [float]: [Retorna metade do valor.]
    """
    res = valor / 2
    return res if not formatar else moeda(res)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')
'''
Exercício Python 110: Adicione o módulo moeda criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
'''
c =(
    '\033[m',              # 0 -> SEM CORES
    '\033[0;30;41m',       # 1 -> VERMELHO
    '\033[0;30;42m',       # 2 -> VERDE
    '\033[0;30;43m',       # 3 -> AMARELO
    '\033[0;30;44m',       # 4 -> AZUL
    '\033[0;30;45m',       # 5 -> ROXO
    '\033[;7m'             # 6 -> INVERTE
)

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


def escreva(frase, cor=0):
    print(c[cor], end='')
    print('=' * 40)
    print(f'{frase:^40}')
    print('=' * 40)
    print(c[0], end='')



def resumo(valor=0, vAumento=0, vDecresc=0):
    """Exibe resumo dos valores a partir da entrada de valor informado.

    Args:
        valor (int, optional): [Valor para trabalho]. Defaults to 0.
        vAumento (int, optional): [Taxa para aumento]. Defaults to 0.
        vDecresc (int, optional): [Taxa para decréscimo]. Defaults to 0.
    """
    resumo = {}
    resumo['Preço analisado'] = f'{moeda(valor):<10}'
    resumo['Dobro do preço'] = f'{dobro(valor=valor, formatar=True)}'
    resumo['Metado do valor'] = f'{metade(valor=valor,formatar=True)}'
    resumo[f'{vAumento}% de aumento'] = f'{aumentar(valor=valor, taxa=vAumento, formatar=True)}'
    resumo[f'{vDecresc}% de redução'] = f'{diminuir(valor=valor, taxa=vDecresc, formatar=True)}'
    escreva('RESUMO DO VALOR', cor=6)
    for chave,valor in resumo.items():
        print(f'{chave:.<20} : {valor:<10}')
    escreva('FIM DO PROGRAMA', cor=6)

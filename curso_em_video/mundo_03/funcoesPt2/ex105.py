'''
Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

– Quantidade de notas                                                                 – A maior nota                                                                  – A menor nota                                                                  – A média da turma                                                                 – A situação (opcional)
'''
import cabecalho


def notas(*n, sit=False):
    """[Função para analisar a nota e situação de vários alunos.]

    Args:
        sit (bool, optional): [Valor opcional para adicionar ou não a situação da média de notas.]. Defaults to False.

    Returns:
        [dict]: [Várias informações sobre a situação da turma.]
    """
    cadNotas = {}
    # Quantidade de notas
    cadNotas['Quantidade de notas'] = len(n)
    # maior, menor e média
    maior = menor = media = soma = 0
    for i,v in enumerate(n):
        soma += v
        if i == 0:
            maior = menor = v
        else:
            if v > maior:
                maior = v
            if v < menor:
                menor = v
    media = soma / len(n)

    # Maior nota
    cadNotas['A maior nota'] = maior
    # Menor nota
    cadNotas['A menor nota'] = menor
    # Média
    cadNotas['A média da turma'] = media
    # Situação
    if sit:
        if media < 5:
            cadNotas['Situação'] = 'RUIM'
        if media >= 5 and media < 7:
            cadNotas['Situação'] = 'RAZOÁVEL'
        elif media >= 7:
            cadNotas['Situação'] = 'BOA'
    return cadNotas

cadastro = notas(5.5, 2.5, 2, 6.5, sit=True)

cabecalho.escreva('CADASTRO DE NOTAS')
for k,v in cadastro.items():
    print(f'{k:<20} : {v}')
cabecalho.escreva('FIM')

help(notas)
# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO.

def voto(nasc):
    """
    Recebe o ano de nascimento de uma pessoa e retorna a situação eleitoral.

    Args:
        nasc ([int]): [Ano de nascimento.]
    """
    from datetime import date

    anoAtual = date.today().year
    idade = anoAtual - nasc
    if idade < 16:
        return f'Idade: {idade} anos, voto NEGADO!'
    elif (idade > 15 and idade < 18) or (idade > 65):
        return f'Idade: {idade} anos, voto OPCIONAL!'
    else:
        return f'Idade: {idade} anos, voto OBRIGATÓRIO!'


nasc = int(input('Digite sua data de nascimento: '))
print(voto(nasc))
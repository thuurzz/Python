# ex_1048_URI

# Tabela de aumento:
# A empresa ABC resolveu conceder um aumento de salários a
# seus funcionários de acordo com a tabela abaixo:
#
# 0 - 400.00 /          15%
# 400.01 - 800.00 /     12%
# 800.01 - 1200.00 /    10%
# 1200.01 - 2000.00 /   7%
# Acima de 2000.00 /    4%

# Leia o salário do funcionário e calcule e mostre o novo salário,
# bem como o valor de reajuste ganho e o índice reajustado, em percentual.
# Entrada***
# A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.
# Saída*****
# Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste e o percentual de reajuste ganho,
# conforme exemplo abaixo.

# lê o salário em float
s = float(input(''))

# tabela de if, com aumento
novo_s = r = p = 0
if s <= 400:  # +15%
    p = 15/100
    novo_s = s + (s * p)
    r = novo_s - s
elif s > 400 and s <= 800:  # +12%
    p = 12/100
    novo_s = s + (s * p)
    r = novo_s - s
elif s > 800 and s <= 1200:  # +10%
    p = 10/100
    novo_s = s + (s * p)
    r = novo_s - s
elif s > 1200 and s <= 2000:  # +7%
    p = 7/100
    novo_s = s + (s * p)
    r = novo_s - s
elif s > 2000:  # +4%
    p = 4/100
    novo_s = s + (s * p)
    r = novo_s - s

# exibes valores reajustados
print(f'''Novo salario: {novo_s:.2f}
Reajuste ganho: {r:.2f}
Em percentual: {int(p * 100)} %''')

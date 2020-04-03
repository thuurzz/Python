sb = float(input('Digite o valor do seu salário: '))
temp = float(input('Digite a quantidades de meses completos na empresa: '))
emp = float(input('Digite o valor almejado de empréstimo: '))

if (sb > 2000):
    if (temp > 24):
        juros = (emp * 0.15)
    else:
        juros = (emp * 0.20)
    print('O valor total devido é de: {.02f}'.format(emp + juros))

else:
    print('Devido a falta de algumas condições, seu empréstimo foi negado!')






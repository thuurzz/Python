print('Olá, digite o valor do salário minimo e seu gasto com água deste mês:')

s_min = float(input('digite o valor do salário minímo:'))
quant_agua  = float(input('digite a quantidade de litros de água consumidos este mês:'))
valor_conta: float = round((s_min*0.02)*(quant_agua/1000),2)
descon_15 = round((valor_conta*0.85),2)

print('Este mês foram utilizados {} litros de água, com valor do salário equivalente a {}, o valor da conta será: {}'.format(quant_agua, s_min, valor_conta))
print('este mês, o valor tera um desconto de 15%, resultando no valor a ser pago de:{}'.format(descon_15))


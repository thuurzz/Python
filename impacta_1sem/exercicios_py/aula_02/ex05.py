print('olá, digite o valor de seu salário mensal e o percentual de aumento deste mês e será exibido o valor total a ser recebido.')

salario = float(input('digite o valor salarial:'))
percentual = float(input('digite o percentual de aumento:'))

salario_final = round((salario) + (salario*(percentual/100)),2)

print('o valor a ser recebido será: {}'.format(salario_final))

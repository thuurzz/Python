print('Olá, digite o valor que você recebe por hora, quantas horas por dia, quantos dias trabalhou e iremos calcular o valor do seu salário mensal!')

valorHora = float(input('digite o valor recebido por hora, utilize ponto caso haja casa decimal:'))
horas = float(input('digite quantas horas por dia trabalhou, utilize ponto caso haja casa decimal:'))
dias = float(input('digite quantos dias trabalhou, utilize ponto caso haja casa decimal:'))

salario = (valorHora*horas)*dias

print('Este mês você trabalhou {} horas, {} dias, logo receberá: {} R$. '.format(horas, dias, salario))

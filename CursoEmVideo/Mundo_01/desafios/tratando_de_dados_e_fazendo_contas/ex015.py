dias = float(input('Digite a quantidade de dias que utilizou o carro: '))
kms = float(input('Digite a quantidade de kms que foram percorridos com o veículo: '))
custo_dias = dias * 60
custo_kms = kms * 0.15
custo_total = (custo_dias + custo_kms)

print('Tendo utilizado o carro por {:.0f} dias e rodado {} km, o custo de utilização foi de {:.2f} R$.'.format(dias, kms, custo_total))

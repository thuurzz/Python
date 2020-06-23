print('olá, por favor informe a quantidade de dias que o carro foi utilziado e quantos km você percorreu:')

dias = float(input('digite a quantidade de dias:'))
km = float(input('digite a quantidade de kms percorridos com o veículo:'))

custo = round((dias*60) + (km*0.15),2)

print("o custo total da utilização do veículo foi: {} R$.".format(custo))

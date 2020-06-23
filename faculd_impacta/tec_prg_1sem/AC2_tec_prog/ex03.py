#Arthur Vinicius Santos Silva RA:1903665

altura = float(input())
peso = float(input())

imc = round((((peso)) / (altura * altura)),2)


if imc < 17:
    print(imc)
    print('Muito abaixo do peso')
elif 17 <= imc < 18.5:
    print(imc)
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print(imc)
    print('Peso normal')
elif 25 <= imc < 30:
    print(imc)
    print('Acima do peso')
elif 30 <= imc < 35:
    print(imc)
    print('Obesidade grau I')
elif 35 <= imc < 40:
    print(imc)
    print('Obesidade grau II')
else:
    print(imc)
    print('Obesidade grau III')

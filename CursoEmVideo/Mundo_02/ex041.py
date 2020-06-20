print('A partir da usa idade, você sera classificado na modalidade adequada.')
idade = int(input('Qual sua idade? '))

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade == 20:
    print('SÊNIOR')
else:
    print('MASTER')
print('Olá, tudo bem? Digite o valor das suas 4 notas para calculo da sua média!')
n1 = int(input('digite o valor da média 1:'))
n2 = int(input('digite o valor da média 2:'))
n3 = int(input('digite o valor da média 3:'))
n4 = int(input('digite o valor da média 4:'))

media = (n1+n2+n3+n4)/4

print('o valor da sua média é: ', media)

if (media > 7):
    print('você foi aprovado!')
else:
    print('se esforçe mais!')


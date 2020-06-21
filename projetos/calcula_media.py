print('Digite o valor das suas notas e diremos se vc passou de semestre: ')

nome = input('Digite seu nome: ')

prova1 = int(input('digite a nota da sua prova1: '))
prova2 = int(input('digite a nota da sua prova2: '))
prova3 = int(input('digite a nota da sua prova3: '))
prova4 = int(input('digite a nota da sua prova4: '))

media = (prova1 + prova2 + prova3 + prova4) / 4

print(f'Sua média foi: {media}')

if media >= 6:
    print(f'Estoro {nome}! ta de férias!')
else:
    print(f'SIFUDEL {nome}')
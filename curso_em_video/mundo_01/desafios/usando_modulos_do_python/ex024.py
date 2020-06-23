#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = input('Digite o no da sua cidade: ').strip()


comeca = cidade.lower()[:5] == 'santo'

if comeca == True:
    print('O nome da sua cidade começa com Santo')
else:
    print('O nome da sua cidade não começa com Santo')
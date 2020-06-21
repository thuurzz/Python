from datetime import date

# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
# alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

sexo = input('''Selecione o seu sexo:
[M] Masculino
[F] Feminino\n''').upper()
if sexo == 'F':
    print('Sexo feminino não exige alistamento no Brasil.')
else:
    nasc = int(input('Digite seu ano de nascimento: '))
    ano_atual = date.today().year
    idade = ano_atual - nasc
    if idade < 18 and sexo == 'M':
        print(f'Você ainda não precisa se alista, faltam {18 - idade} anos.')
    elif idade == 18 and sexo == 'M':
        print('Você deve se apresentar ao alistamento!')
    elif idade > 18 and sexo == 'M':
        print(f'Você esta atrasado {idade - 18} anos para o alistamento! Se apresente o quanto antes!')


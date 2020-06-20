idade = int(input('Digite a sua idade e serão exibidas informações sobre o alistamento militar:'))

if idade < 18:
    print(f'Você ainda não precisa se alista, faltam {18 - idade} anos.')
elif idade == 18:
    print('Você deve se apresentar ao alistamento!')
else:
    print(f'Você esta atrasado {idade - 18} anos para o alistamento! Se apresente o quanto antes!')

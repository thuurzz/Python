# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
#
# – Média abaixo de 5.0: REPROVADO
#
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
#
# – Média 7.0 ou superior: APROVADOExercício Python 040: Crie um programa que leia duas notas de um aluno e
#  calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

print('Digite o valor das suas notas e diremos se vc passou de semestre: ')

nome = input('Digite seu nome: ')

prova1 = float(input('digite a nota da sua prova 1: '))
prova2 = float(input('digite a nota da sua prova 2: '))

media = (prova1 + prova2) / 2

print(f'Sua média foi: {media}')

if media < 5:
    print(f'{nome},você foi reprovado!')
elif 5 < media < 6.9:
    print('Você esta de recuperação!')
else:
    print('APROVADO!')

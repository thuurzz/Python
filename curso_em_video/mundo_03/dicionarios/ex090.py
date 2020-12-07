# Exercício Python 090: Faça um programa que leia Nome e média de um aluno, guardando também a Situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = {}
aluno['Nome'] = input('Nome do aluno: ')
aluno['Media'] = float(input('Media: '))

if aluno['Media'] < 5:
    aluno['Situação'] = 'Reprovado'
elif aluno['Media'] >= 5 and aluno['Media'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Aprovado'

print('-=' * 20)
for key,val in aluno.items():
    print(f'- {key} é igual a {val}')
print('-=' * 20)
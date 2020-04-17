'''
Dado a quantidade de alunos de uma turma, calcular a média semestral de cada aluno e
mostrar uma mensagem para os alunos aprovados.
'''

t_alunos = int(input('Digite a quantidade de alunos: '))

i = 1

while i <= t_alunos:
    nome = input('Digite o nome do aluno: ')
    n1 = float(input('digite  a nota da primeira prova: '))
    n2 = float(input('digite  a nota da segunda prova: '))
    media = (n1 + n2) / 2
    i = i + 1

    if media >= 6:
        print('A nota do aluno {}, foi {}, logo este foi aprovado!'.format(nome, media))
    else:
        print('A nota do aluno {}, foi {}, logo este foi reprovado!'.format(nome, media))


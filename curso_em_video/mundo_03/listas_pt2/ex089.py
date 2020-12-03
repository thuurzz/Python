#EX089.py

bd_alunos = list()

while True:
    # Lê dados dos alunos
    nome = input('Nome do aluno:')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    # Coloca nome na lista
    bd_alunos.append([nome, [nota1, nota2]])
    # Deseja continuar?
    opc = input('Deseja continuar?[S/N]: ')
    if opc in 'Nn':
        break

print('-' * 35)
print(f'{"NUM":<10}{"NOME":<20}{"MÉDIA":<10}')
print('-' * 35)
for num,aluno in enumerate(bd_alunos):
    print(f'{num:<10}{aluno[0]:<20}{sum(aluno[1])/len(aluno[1]):<10}')
print('-' * 35)
while True:
    procuraAluno = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if procuraAluno == 999:
        break
    print(f'As notas do(a) aluno: {bd_alunos[procuraAluno][0]}, foram: {bd_alunos[procuraAluno][1]}')
print('-' * 35)
print('FIM DO PROGRAMA')



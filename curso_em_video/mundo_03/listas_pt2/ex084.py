#EX084
pessoa = list()
BD_cadastro = list()
# Lê nome e peso de várias pessoas
while True:
    nome = input('Nome:')
    pessoa.append(nome)
    peso = float(input('Peso:'))
    pessoa.append(peso)
    BD_cadastro.append(pessoa[:])
    pessoa.clear()
    # Deseja continuar?
    opc = input('Deseja continuar?[S/N]: ')
    if opc in 'Nn':
        break

# define maior e menor peso
maiorPeso = menorPeso = 0
for i in range(len(BD_cadastro)):
    if i == 0:
        maiorPeso = menorPeso = BD_cadastro[i][1]
    else:
        if BD_cadastro[i][1] > maiorPeso:
            maiorPeso = BD_cadastro[i][1]
        if BD_cadastro[i][1] < menorPeso:
            menorPeso = BD_cadastro[i][1]

# quantas pessoas foram cadastradas?
print(f'Foram cadastradas {len(BD_cadastro)} pessoa(s) na lista.')
# listagem com as pessoas com maior peso
print('As pessoas com maior peso, são:')
for ser  in BD_cadastro:
    if ser[1] == maiorPeso:
        print(f'Nome: {ser[0]} e Peso: {ser[1]}')
# listagem com as pessoas com menor peso
print('As pessoas com menor peso, são:')
for ser  in BD_cadastro:
    if ser[1] == menorPeso:
        print(f'Nome: {ser[0]} e Peso: {ser[1]}')

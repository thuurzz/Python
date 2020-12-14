# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

cadastro = []
while True:
    # Lê nome, sexo de idade de vários
    pessoa = {}
    # Lê nome
    pessoa['Nome'] = str(input('Nome: '))

    # Lê sexo e valida
    pessoa['Sexo'] = str(input('Sexo[M/F]: ')).upper()
    while pessoa['Sexo'] not in 'MF':
        pessoa['Sexo'] = str(input('Opção invalida [M/F]: ')).upper()

    # Lê idade 
    pessoa['Idade'] = int(input('Idade: '))

    # Coloca a pessoa na lista de cadastro
    cadastro.append(pessoa.copy())

    # Pergunta se continua
    opc = str(input('Deseja continuar? [S/N]: ')).lower()
    while opc not in 'sn':
        opc = str(input('Opção invalida [S/N]: ')).lower()
    if opc == 'n':
        break

print(f'{" CADASTRO ":=^30}')
# A) Quantas pessoas foram cadastradas
print(f'A) Ao todo temos {len(cadastro)} pessoas cadastradas.')
print('=' * 30)

# B) A média de idade
soma = media = 0
for pessoa in cadastro:
    soma += pessoa['Idade']
media = soma / len(cadastro)
print(f'B) A média de idade é: {media}')
print('=' * 30)

# C) Uma lista com as mulheres
print('C) Lista com as mulheres:')
for pessoa in cadastro:
    if pessoa['Sexo'] == 'F':
        print(pessoa['Nome'])
print('=' * 30)

# D) Uma lista de pessoas com idade acima da média
print('D) Lista de pessoas com idade acima da média:')
for pessoa in cadastro:
    if pessoa['Idade'] > media:
        print(f'Nome: {pessoa["Nome"].upper()} Sexo: {pessoa["Sexo"]} Idade: {pessoa["Idade"]}')
print(f'{" FIM DO PROGRAMA ":=^30}')
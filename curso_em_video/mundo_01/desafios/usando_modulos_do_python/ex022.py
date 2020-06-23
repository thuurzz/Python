nome = input('Digite seu nome completo: ').strip()

# maiúsculas
print('Seu nome em letras maiúsculas:')
print(nome.upper())

# minúsculas
print('Seu nome em letas minúsculas: ')
print(nome.lower())

# tamanho
so_letras = len(nome) - nome.count(' ')
print(f'Seu nome tem {so_letras} letras.')

#tamanho primeiro nome
print(f'Seu primeiro nome tem {nome.find(" ")} letras:')



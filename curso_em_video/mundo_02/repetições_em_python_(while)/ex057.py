# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação
# novamente até ter um valor correto.


# usando comparação (==)

sexo = input('Esolha a opção: [M]Masculino [F]Feminino: ').strip().upper()[0]
# enquanto sexo NÃO for M ou F, pede novamente.

while not ('F' == sexo or 'M' == sexo):
    print('Opção invalida, tente novamente.')
    sexo = input('[M]Masculino [F]Feminino: ').strip().upper()

# Se F ou M, exibe sexo selecionado.
if sexo == 'F':
    print('Sexo feminino selecionado!')
elif sexo == 'M':
    print('Sexo masculino selecionado!')
    

print('=' * 50)


# usando função (in)

sexo = input('Esolha a opção: [M]Masculino [F]Feminino: ').strip().upper()[0]
# enquanto sexo NÃO for M ou F, pede novamente.
# usando comparação
while not sexo in 'MF':
    print('Opção invalida, tente novamente.')
    sexo = input('[M]Masculino [F]Feminino: ').strip().upper()

# Se F ou M, exibe sexo selecionado.
if sexo == 'F':
    print('Sexo feminino selecionado!')
elif sexo == 'M':
    print('Sexo masculino selecionado!')

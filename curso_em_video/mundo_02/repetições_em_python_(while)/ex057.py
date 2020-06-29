sexo = input('Esolha a opção: [M]Masculino [F]Feminino: ').strip().upper()
# enquanto sexo NÃO for M ou F, pede novamente.
while not ('F' == sexo[0] or 'M' == sexo[0]):
    print('Opção invalida, tente novamente.')
    sexo = input('[M]Masculino [F]Feminino: ').strip().upper()

# Se F ou M, exibe sexo selecionado.
if sexo[0] == 'F':
    print('Sexo feminino selecionado!')
elif sexo[0] == 'M':
    print('Sexo masculino selecionado!')

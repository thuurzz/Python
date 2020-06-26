print('Digite uma frase para verificar se é um PALINDROMO: ')
frase = input('Digite sua frase: ').strip(' ')

# APOS A SOPA
# for i in range(len(frase)):

if frase == frase[::-1]:
    print('Esta frase é um PALINDROMO!')
else:
    print('Esta frase não é um PALINDROMO!')

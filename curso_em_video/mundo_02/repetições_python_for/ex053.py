print('Digite uma frase para verificar se é um PALINDROMO.')
frase = input('Digite sua frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print('Esta frase é um PALINDROMO!')
else:
    print('Esta frase não é um PALINDROMO!')

'''
if frase == frase[::-1]:
    print('Esta frase é um PALINDROMO!')
else:
    print('Esta frase não é um PALINDROMO!')
'''

# APOS A SOPA

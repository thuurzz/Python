# ex077.py

# texto com palavras
palavras = 'Nessa aula vamos aprender TUPLAS como utilizar tuplas Python tuplas compostas e  que permitem armazenar valores em uma mesma estrutura por chaves individuais'

# transforma em tupla
palavras = palavras.split()

for palv in palavras:
    vogais = ''
    for letra in palv:
        if letra == 'a':
            vogais += 'a'
        elif letra == 'e':
            vogais += 'e'
        elif letra == 'i':
            vogais += 'i'
        elif letra == 'o':
            vogais += 'o'
        elif letra == 'u':
            vogais += 'u'
       
    print(f'Na palavara {palv.upper()} temos as vogais: {vogais}.')
# ex077.py

# texto com palavras
palavras = 'Nessa aula vamos aprender tuplas como utilizar tuplas python tuplas compostas que permitem armazenar valores em uma mesma estrutura por chaves individuais'

# transforma em tupla
palavras = palavras.split()

for palv in palavras:
    vogais = ''
    for letra in palv:
        if letra.lower() in 'aeiou':
            vogais += letra
    print(f'Na palavara {palv.upper()} temos as vogais: {vogais}.')
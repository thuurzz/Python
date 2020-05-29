# Qual das alternativas é a função adequada para o cálculo da média
# aritmética simples no código abaixo? (OBS: Após a leitura das
# notas digitadas pelo usuário, a média deve ser exibida na tela
# uma única vez).

# Função 9:
def calcula_media(n1, n2, n3):
    resultado = (n1 + n2 + n3) / 3
    return resultado


a = float(input('nota 1: '))
b = float(input('nota 2: '))
c = float(input('nota 3: '))
media = calcula_media(a, b, c)
print(media)

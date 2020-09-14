# URI Online Judge | 1079

# Leia 1 valor inteiro N
n = int(input())

nota = total = 0
# repete o teste quantas vezes n(entrada) pedir
for i in range(n):
    # pede em string
    nota = input()
    # separa pelos espaços
    nota = nota.split()
    # coloca cada entrada em uma var, cada um com um peso
    n1 = float(nota[0]) * 2
    n2 = float(nota[1]) * 3
    n3 = float(nota[2]) * 5
    # soma as notas após multiplicação por peso
    # divide por 10 (2 + 3 + 5) conforme peso da documentação
    mp = round((n1 + n2 + n3) / 10, 1)
    # exibe resultado
    print(mp)



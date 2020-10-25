# URI Online Judge | 1211
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1211

# inicia o looping até que o usuário digite 0 nas quantidades de numeros
while True:
    try:
        # Quantidade de telefones
        n = int(input())

        # Inicia lista e adiciona telefones
        lTel = []
        for i in range(n):
            tel = input()
            lTel.append(tel)

        econ = 0
        for i in range(len(lTel) - 1):
            for tel in range(len(lTel[i])):
                if lTel[i][0] == lTel[i + 1][0]:
                    if lTel[i][tel] == lTel[i + 1][tel]:
                        econ += 1

        print(econ)
    except EOFError:
        break
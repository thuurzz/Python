#URI 1252

while True:
    N, M = map(int, input().split())
    print(N, M)
    
    par_num, impar_num = [], []
    par_qtd, impar_qtd = [], []
    par, impar = [], []

    for y in range(N):
        numb = int(input())
        if numb < 0 and numb % M != 0:
            resto = numb % M - M
        elif numb >= 0 or (numb < 0 and numb % M == 0):
            resto = numb % M

        if numb % 2 != 0:
            impar_num.append(numb)
            impar_qtd.append(resto)
        else:
            par_num.append(numb)
            par_qtd.append(resto)

    for i in range(len(impar_num)):
        impar.append((impar_num[i], impar_qtd[i]))
    for p in range(len(par_num)):
        par.append((par_num[p], par_qtd[p]))

    impar.sort(key=lambda x: int(x[0]), reverse=True)
    impar.sort(key=lambda x: int(x[1]))
    par.sort(key=lambda x: int(x[0]))
    par.sort(key=lambda x: int(x[1]))
    final = impar + par
    final.sort(key=lambda x: int(x[1]))

    for a in range(len(final)):
        print(final[a][0])

    if N == M == 0:
        break

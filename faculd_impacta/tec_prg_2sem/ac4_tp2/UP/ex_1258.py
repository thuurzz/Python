# URI Online Judge | 1258
final=[]
while True:
    # Pede quantidade de camisetas enquanto != 0
    n = int(input())
    if n == 0:
        break

    # Cria vetor(nome, cor e tamanho)
    qtCam = [[0,0,0] for i in range(n)]

    # Pede nome, tamanho e cor e atribui no vetor
    for i in range(len(qtCam)):
        #pede o nome
        nome = input()
        #pede cor e tamanho e separa
        corTam = input().split()
        cor = corTam[0]
        tam = corTam[1]
        #preenche no vetor
        qtCam[i][0] = nome
        qtCam[i][1] = cor
        qtCam[i][2] = tam
        # qtCam = [[nome, cor, tam]]
    qtCam.sort(key=lambda x:x[0])
    qtCam.sort(key=lambda x:x[2], reverse=True)
    qtCam.sort(key=lambda x:x[1])
    final.append(qtCam)

loop = 0
for i in final:
    loop += 1
    for j in i:
        print(j[1], j[2], j[0],)
    if loop != len(final):  
        print()
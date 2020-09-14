# URI Online Judge | 1235

# número de casos
nCasos = int(input())

for i in range(nCasos):
    texto = input()
    meio = int(len(texto)/2)
    #print(meio)
    txt1 = texto[:meio]
    #print(txt1[::-1])
    txt2 = texto[meio:]
    #print(txt2[::-1])
    print(''.join(txt1[::-1]+txt2[::-1]))

#L.E.V.E.L.K.A.Y.A.K
#0.1.2.3.4.5.6.7.8.9FU
#preenche lista vazia com valores da matriz m, caso inidices sejam pares.

m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
ql = len(m)
qc = len(m[0])
l = []
for i in range(ql):
    for j in range(qc):
        if (i % 2) == 0 and (j % 2) == 0:
            l.append(m[i][j])
print(l)

# resposta: [1, 3, 9, 11]

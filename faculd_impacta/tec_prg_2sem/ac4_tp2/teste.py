lTel = ['12121212', '01112222']
econ = 0
for i in range(len(lTel)-1):
    for tel in range(4):
        if lTel[i][0] == lTel[i+1][0]:
            if lTel[i][tel] == lTel[i+1][tel]:
                econ += 1

print(econ)
            
            
 
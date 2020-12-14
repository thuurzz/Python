#EX080


lNum = []
for i in range(5):
    n = int(input('Digite um valor: '))
    if i == 0 or n > lNum[-1]:
        lNum.append(n)
        print('Adiconado ao final da lista.')
    else:
        for pos,num in enumerate(lNum):
            if n <= num:
                lNum.insert(pos,n)
                print(f'Número {n} adiconado na posicão {pos}.')
                break
            
print(f'A lista de valores é: {lNum}')
# URI Online Judge | 1241

# Lê quantidade de repetições
n = int(input())

for i in range(n):
    lNum = input().split()
    n1 = lNum[0]
    n2 = lNum[1]

    if n2 == n1[(len(n1) - len(n2)):]:
        print('encaixa')
    else:
        print('nao encaixa')
   
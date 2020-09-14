#URI Online Judge | 1192

# quantidade de testes
nTestes = int(input())

for i in range(nTestes):
    total = 0
    # lê código e separa digitos
    cod = input()
    letra = cod[1]
    dig1 = cod[0]
    dig2 = cod[2]

    if letra.isupper() and dig1 != dig2:
        total = int(dig2) - int(dig1)
    elif letra.islower() and dig1 != dig2:
        total = int(dig1) + int(dig2)
    elif dig1 == dig2:
        total = int(dig1) * int(dig2)
    print(total)

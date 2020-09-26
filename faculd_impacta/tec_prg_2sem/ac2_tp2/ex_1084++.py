while True: # O programa fica em loop ate entrar num == 0 e dig == 0
    num, dig = input().split()
    num = int(num)
    dig = int(dig)

    if num == 0 and dig == 0:
        break

    seq = list(input())
    atual = 0 #valor de digito atual a ser removido (tenta retirar 0s primeiro, depois 1s, 2s....)
    i = 0 #iterador para o número de digitos a serem removidos
    while i < dig:
        cont = 0
        while cont < len(seq):
            if i >= dig:
                break
            elif seq[cont] == str(atual):
                del seq[cont]
                i += 1
                cont -= 1
            cont += 1
        atual += 1

    print(''.join(seq))
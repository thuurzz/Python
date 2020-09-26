while True: # O programa fica em loop ate entrar num == 0 e dig == 0
    num, dig = input().split()
    num = int(num)
    dig = int(dig)

    if num == 0 and dig == 0:
        break

    # entrada com sequência de números
    seq = list(input())
        # lista dos que serão retirados
    retirados = 0
    # loop do tamanho da sequência
    for i in range(num):
        # retira o menor da verificação dele e do próximo tantas vezes quanto o {dig} indicar
        while dig > 0:
            if int(seq[i]) > int(seq[i + 1]):
                dig -= 1
                seq.pop(i+1)
            else: 
                dig -=1
                del seq[i]
    # verifica se a quantidade de retirados é menor que a proposta, faz a diferença e retira os últimos
        while dig > 0:
            seq.pop()
            dig-=1
    # exibe sequência restante
    print(''.join(seq))
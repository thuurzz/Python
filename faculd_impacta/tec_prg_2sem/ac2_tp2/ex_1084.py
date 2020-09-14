# URI Online Judge | 1084

while True: # O programa fica em loop ate entrar num == 0 e dig == 0
    numDig = input().split()
    num = int(numDig[0])
    dig = int(numDig[1])
    if num == 0 and dig == 0:
        break

    # entrada com sequência de números
    seqStr = input()
    seq = []
    for alg in seqStr:
        seq.append(int(alg))

    # lista dos que serão retirados
    retirados = 0
    # loop do tamanho da sequência
    for i in range(num):
        # retira o menor da verificação dele e do próximo tantas vezes quanto o {dig} indicar
        while retirados < dig:
            if seq[i] > seq[i + 1]:
                retirados += 1 
                del seq[i+1]
            else: 
                retirados += 1 
                del seq[i]
    # verifica se a quantidade de retirados é menor que a proposta, faz a diferença e retira os últimos
    if retirados < dig:
        faltou = retirados - dig
        for i in range(faltou):
            del seq[-1]
    # exibe sequência restante
    final = []
    for item in seq:
        final.append(str(item))

    print(''.join(final))
    



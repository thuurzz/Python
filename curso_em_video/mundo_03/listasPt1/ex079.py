#EX079

# cria lista
lNum = []

# Pede num e coloca na lista se já não tiver
while True:
    n = int(input('Digite um valor: '))
    if n not in lNum:
        lNum.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor não adiconado pois já consta na lista!')

    # pergunta se deseja continuar
    opc = input('Desja continuar? [S/N]').lower()
    while opc not in 'sn':
        opc = input('Tente de novo, deseja continuar? [S/N]').lower()
    # se digita 'n' para de pedir valores
    if opc == 'n':
        break

# coloca em ordem crescente
lNum.sort()

# exibe resultado
print(f"A lista de valores é: {lNum}")

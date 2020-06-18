# contas do mês

#faz as contas da casa
def soma_casa():
    casa = []
    while True:
        valor = float(input('Digite o valor a ser somado, digite 0 ao término: '))
        if valor == 0:
            break
        casa.append(valor)
    total_casa = sum(casa)
    print(f'Os valores foram:{casa} o valor das contas da casa é: {total_casa}R$')
    return total_casa


#faz a conta do membro e soma a da casa divida para cada um
def soma_rone(total_cs):
    rone = []
    while True:
        valor = float(input('Digite o valor a ser somado, digite 0 ao término: '))
        if valor == 0:
            break
        rone.append(valor)
    total_rone = sum(rone) + (total_cs / 3)
    print(f'Os valores foram:{rone}, somados as contas da casa dividas, no valor de {total_cs / 3} o valor total para Rone é: {total_rone}')
    return total_rone


#faz a conta do membro e soma a da casa divida para cada um
def soma_bia(total_cs):
    bia = []
    while True:
        valor = float(input('Digite o valor a ser somado, digite 0 ao término: '))
        if valor == 0:
            break
        bia.append(valor)
    total_bia = sum(bia) + (total_cs / 3)
    print(f'Os valores foram:{bia}, somados as contas da casa dividas, no valor de {total_cs / 3} o valor total para Bia é: {total_bia}')
    return total_bia


#faz a conta do membro e soma a da casa divida para cada um
def soma_loze(total_cs):
    loze = []
    while True:
        valor = int(input('Digite o valor a ser somado, digite 0 ao término: '))
        if valor == 0:
            break
        loze.append(valor)
    total_loze = sum(loze)
    print(f'Os valores foram:{loze}, somados as contas da casa dividas, no valor de {total_cs / 3} o valor total para Loze é: {total_loze}')
    return total_loze

def soma_inquilino():
    a = float(input('digite o valor da conta de água: '))
    l = float(input('digite o valor da conta de luz: '))
    i = 20
    total  = (a / 6) + (l / 2) + i
    total = round(total)
    print(f'O valor total para cada inquilino é de {total}')


print('Defina os valores da Casa para divisão aos outros membros!')
total_cs = soma_casa()

while True:
    membro = float(input('Selecione o membro da casa para fazer as contas:[1]Bia [2]Loze [3]Rone [4]Inquilino [0]Finalizar: \n'))
    if membro == 1:
        soma_bia(total_cs)
    elif membro == 2:
        soma_loze(total_cs)
    elif membro == 3:
        soma_rone(total_cs)
    elif membro == 4:
        soma_inquilino()
    else:
        break
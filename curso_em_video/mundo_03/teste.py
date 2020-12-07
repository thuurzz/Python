opc = str(input('Deseja continuar? [S/N] ')).lower()
while opc not in 'sn':
    opc = str(input('Opção invalida [S/N] ')).lower()
    if opc == 'n':
        break
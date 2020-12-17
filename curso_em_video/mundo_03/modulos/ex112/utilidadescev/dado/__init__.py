def leiaDinheiro(msg):
    while True:
        valor = input(msg).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print('\033[0;31mERRO! Digite um valor monetário.\033[m')
        else:
            break
    return float(valor)

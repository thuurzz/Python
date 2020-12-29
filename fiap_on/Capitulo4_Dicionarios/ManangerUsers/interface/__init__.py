def menu(list):
    titulo('MENU')
    print('Selecione umas das opções abaixo: ')
    c = 1
    for item in list:
        print(f'{c} - {item}')
        c += 1
    while True:
        try:
            opt = int(input('Digite a opção desejada: '))
            if opt > len(list):
                print('Escolha entre as opções apresentadas.')
            else:
                return  int(opt)
        except:
            print('Opção inválida, tente novamente!')
    

def linha():
    print('=' * 42)


def titulo(msg):
    linha()
    print(f'{msg:^42}')
    linha()
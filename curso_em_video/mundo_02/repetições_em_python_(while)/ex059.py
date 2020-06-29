print('Digite dois valores, depois selecione a opção desejada.')
n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))

opc = int(input('''Digite a operação desejada:
[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa\n'''))

while not opc == 5:
    if opc == 1:
        soma = n1 + n2
        print(f'A soma dos valores é: {soma}')
        print('=' * 30)
        opc = int(input('''Digite a operação desejada:
        [1]somar
        [2]multiplicar
        [3]maior
        [4]novos números
        [5]sair do programa\n'''))
    elif opc == 2:
        mult = n1 * n2
        print(f'A multiplicação dos valores é: {mult}')
        print('=' * 30)
        opc = int(input('''Digite a operação desejada:
        [1]somar
        [2]multiplicar
        [3]maior
        [4]novos números
        [5]sair do programa\n'''))
    elif opc == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print(f'O maior destes 2 números é: {maior}')
        print('=' * 30)
        opc = int(input('''Digite a operação desejada:
        [1]somar
        [2]multiplicar
        [3]maior
        [4]novos números
        [5]sair do programa\n'''))
    elif opc == 4:
        n1 = int(input('Digite o 1º valor: '))
        n2 = int(input('Digite o 2º valor: '))
        print('=' * 30)
        opc = int(input('''Digite a operação desejada:
        [1]somar
        [2]multiplicar
        [3]maior
        [4]novos números
        [5]sair do programa\n'''))
print('Progrma finalizado.')
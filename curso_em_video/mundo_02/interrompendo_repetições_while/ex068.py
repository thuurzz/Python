import random, time

# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

print(20 * '=-')
print('JOGO DO IMPAR OU PAR!')
print(20 * '=-')

vit = 0
while True:
    # jogador escolhe par ou impar! O outro é atribuido ao PC.
    jog = int(input('ESOLHA: [1]IMPAR! [2]PAR!'))
    pc = ''
    while not (jog == 1 or jog == 2):
        jog = int(input('ESOLHA: [1]IMPAR! [2]PAR!'))

    if jog == 1:
        jog = 'IMPAR!'
        pc = 'PAR!'

    elif jog == 2:
        jog = 'PAR!'
        pc = 'IMPAR'

    # apresenta escolhas
    print('....PROCESSANDO!')
    time.sleep(2)
    print(f'Jogador escolheu: {jog}')
    print(f'PC escolheu: {pc}')

    # cria número ramdom para par ou impar
    n_pc = random.randint(0, 5)

    # pede número ao jogador, define par ou impar
    while True:
        n_jog = int(input('Escolha um número de 0 a 5!'))
        if 0 <= n_jog <= 5:
            break

    # exibe delay
    print('IMPAR...')
    time.sleep(1)
    print('OU..')
    time.sleep(1)
    print('PAR!')

    # soma total e verifica se impar ou par
    total_n = n_jog + n_pc
    total = ''
    if total_n % 2 == 0:
        total = 'PAR!'
    else:
        total = 'IMPAR!'
    print(f'Jogador escoheu {n_jog} e PC: {n_pc}.')
    print(f'RESULTADO = {total}')

    # compara com total e mostra vencedor
    if total == jog:
        print('\33[7mJogador venceu!\33[m')
        vit += 1
    else:
        print('\33[7mPC venceu!\33[m')
        print(f'Após {vit} vitórias, jogador perdeu essa!')
        break

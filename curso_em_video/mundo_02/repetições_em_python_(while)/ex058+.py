import random

# gera número secreto
num_sec = random.randint(0, 10)
print(num_sec)
print('Sou seu computador, pensei em um número de 0 a 10, sera que você consegue adivinhar?')

# pede número do usuário para comparação
acertou = False
tentativas = 0
while not acertou:
    n = int(input('Faça seu palpite: '))
    tentativas += 1
    if n == num_sec:
        print(f'Parabéns, você acertou! O número secreto é: {num_sec}')
        print(f'Você utilizou {tentativas} tentativas.')
        acertou = True
    elif n != num_sec:
        if n < num_sec:
            print('Um pouco mais...')
        else:
            print('Um pouco menos...')


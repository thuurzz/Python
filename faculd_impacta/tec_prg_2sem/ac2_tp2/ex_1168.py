# URI Online Judge | 1168

# dicionário com valor de leds para construir número
led = {'1':2, '2':5, '3':5, '4':4, '5':5, '6':6, '7':3, '8':7, '9':6, '0':6}

# números de caso teste
n = int(input())


for i in range(n):
    totLeds = 0
    # lê sequência de numéros a serem construíudos
    seqNum = input()
    # itera sequência e soma valores em totLeds
    for num in seqNum:
        totLeds += led[num]
    # exibe valor    
    print(f'{totLeds} leds')
for i in range(6):
    distancia = float(input())

    if distancia < 10:
        print('Muito próximo')
    elif distancia <= 12:
        print('Pŕoximo')
    elif distancia <= 26:
        print('Distância moderada')
    elif distancia <= 50:
        print('Longe')
    else:
        print('Muito longe')


'''
Qual a saída esperada com valores: 50,25,10,51,9?
distancia de 50
Longe

distancia de 25
Distância moderada

distancia de 10
Pŕoximo

distancia de 51
Muito longe

distancia de 9
Muito próximo
'''

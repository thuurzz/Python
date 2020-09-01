# URI Online Judge | 1096

# inicia contadores conforme documentação
i = 1 
j = 7
# contador até 9 
while i <= 9:
    # loop que decresce 7 a 5
    while j > 4:
        print(f'I={i} J={j}')
        j -= 1
    # quando j chega a 4, retorna 7
    if j == 4:
        i += 2
        j = 7
            
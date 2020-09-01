# URI Online Judge | 1097

# inicia contadores conforme documentação
i = 1 
j = 7
k = 3
# contador até 9 
while i <= 9:
    # loop que decresce 7 a 5
    while k > 0:
        print(f'I={i} J={j}')
        j -= 1
        k -= 1
    # quando j chega a 4, retorna 7
    i += 2
    j += 5
    k += 3
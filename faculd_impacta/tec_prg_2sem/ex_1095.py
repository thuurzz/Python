# URI Online Judge | 1095

# inicia contadores conforme documentação
i = 1 
j = 60

#loop até j = 0
while True:
    if j >= 0:
        print(f'I={i} J={j}')
        i += 3
        j -= 5
    # quando j = 0 para o loop
    else:
        break
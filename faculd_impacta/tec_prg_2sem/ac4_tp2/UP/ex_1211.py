# URI Online Judge | 1211
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1211

# inicia o looping até EOFError
while True:
    try:
        # Quantidade de telefones
        n = int(input())

        # Inicia lista e adiciona telefones
        lTel = []
        for i in range(n):
            tel = input()
            lTel.append(tel)
        # implementar algoritmo de ordenação mais eficiente
        lTel.sort() 
        

        econ = 0
        # Passeia pela lista de telefones.
        for i in range(1, len(lTel), 1):
            # Passeia pelos caracteres.
            for j in range(len(lTel[0])):
                # verifica se o primeiro caractere do de cima e de baixo, são iguais.
                if lTel[i][0] == lTel[i-1][0]:
                    # Tendo primeiro caractere igual, testa os outros.
                    if lTel[i][j] == lTel[i-1][j]:
                        # Cada caractere igual, que não será impresso, adiciona +1 para a acumuladora.
                        econ += 1
                    else:
                        # Se identificar caractere diferente, para e vai pro próximo.
                        break
        # Exibe quantidade de caracteres economizados a cada loop
        print(econ)
    except EOFError:
        break

#Arthur Vinicius Santos Silva RA:1903365

# Escreva a funcao checa_quantidade_divisores(n, qtd) na sequencia:
def checa_quantidade_divisores(n, qtd):
    i = 1
    tem_div = False
    qtd_div = 0

    while i <= n:
        if n % i == 0:
            qtd_div += 1

        i += 1

    if qtd_div == qtd:
        tem_div = True

    return tem_div

# Programa principal (ja implementado, voce nao precisa se preocupar com o codigo partir deste ponto)
n = int(input())
qtd = int(input())
if checa_quantidade_divisores(n, qtd):  # se a funcao devolve True, entao...
    print(n, "possui", qtd, "divisores")
else:
    print(n, "nao possui", qtd, "divisores")

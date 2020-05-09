# Escreva a funcao checa_quantidade_divisores(n, qtd) na sequencia:
def checa_quantidade_divisores(n, qtd):
    qtd_divisores = 0
    i = 1
    divisor = False

    while i <= n:
        if (n % i) == 0:
            qtd_divisores += 1
        i += 1

    if qtd == qtd_divisores:
        divisor = True

    return divisor

# Programa principal (ja implementado, voce nao precisa se preocupar com o codigo partir deste ponto)
n = int(input())
qtd = int(input())
if checa_quantidade_divisores(n, qtd): # se a funcao devolve True, entao...
	print(n, "possui", qtd, "divisores")
else:
	print(n, "nao possui", qtd, "divisores")

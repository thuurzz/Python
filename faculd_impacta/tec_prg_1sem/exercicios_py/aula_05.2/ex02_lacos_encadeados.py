#testa se é primo
n = int(input('informe n: '))
qtd_div = 0 #var acumuladora
i = 1 #var contadora

while i <= n:
    sobra_zero = (n % i) #verifica se sobra 0
    if sobra_zero == 0: #se sobra 0
        qtd_div += 1 #acumula 1 ponto
    i += 1

if qtd_div == 2: #caso apenas 2 divisores, é primo!
    print(f'{n} é primo!')
else:
    print(f'{n} não é primo!')


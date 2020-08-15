#URI 1051
# lê o salário em float
s = float(input(''))

# tabela de if, com valor do imposto
ir = 0
faixa1 = 0
faixa2 = 0
faixa3 = 0
if s <= 2000:  # isento
    ir = 'Isento'
else:
    s -= 2000 # tira 2.000 que é a faixa isenta
    while s > 0:
        if s > 2500:
            faixa3 += 1
            s -= 1
        if s > 1000 and s <= 2500:
            faixa2 += 1
            s -= 1
        if s > 0 and s <= 1000:
            faixa1 += 1
            s -= 1
    faixa1 = faixa1 * (8 / 100)
    faixa2 = faixa2 * (18 / 100)
    faixa3 = faixa3 * (28 / 100)
    ir = faixa1 + faixa2 + faixa3


if ir == 'Isento':
    print(ir)
else:
    print(f'R$ {ir}')

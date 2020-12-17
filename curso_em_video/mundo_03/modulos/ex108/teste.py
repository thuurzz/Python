import moeda

# Programa principal
p = float(input('Digite o valor R$: '))
tx = float(input('Digite o valor da taxa: '))
print(f'A metade de {moeda.moeda(p)} é: {(moeda.metade(p, True))}')
print(f'O dobro de {moeda.moeda(p)} é: {moeda.moeda(moeda.dobro(p))}')
print(f'O valor de {moeda.moeda(p)} com taxa de {tx}% é: R${moeda.moeda(moeda.aumentar(p,tx))}')

import moeda

# Programa principal
p = float(input('Digite o valor R$: '))
tx = float(input('Digite o valor da taxa: '))
print(f'A metade de R${p} é: R${moeda.metade(p)}')
print(f'O dobro de R${p} é: R${moeda.dobro(p)}')
print(f'O valor de R${p} com taxa de {tx}% é: R${moeda.aumentar(p,tx)}')

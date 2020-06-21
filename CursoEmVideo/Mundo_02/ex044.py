# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
#
# – à vista dinheiro/cheque: 10% de desconto
#
# – à vista no cartão: 5% de desconto
#
# – em até 2x no cartão: preço formal
#
# – 3x ou mais no cartão: 20% de juros

valor = float(input('Digite o valor do produto: '))
avista = valor * 90/100
cartao = valor * 95/100
cartao2x = valor
cartao3x = valor * 120/100

pagamento = int(input('''Digite a forma de pagamento:
[1]À vista
[2]Cartão
[3]2x no cartão
[4]3x ou mais\n'''))
total = 0
if pagamento == 1:
    total = avista
elif pagamento == 2:
    total = cartao
elif pagamento == 3:
    total = cartao2x
    parcela = total / 2
    print(f'Sua compra será parceladada em 2X sem juros, cada parcela terá o valor de :{parcela}')
elif pagamento == 4:
    total = cartao3x
    qdt_parcelas = int(input('Digite a quantidade de parcelas: '))
    parcela = total / qdt_parcelas
    print(f'Sua compra será parceladada em 2X com juros, cada parcela terá o valor de :{parcela}')
print(f'O valor final do pagamento será: {total:.2f}R$ e teve uma diferença de: {total - valor:.2f}R$')

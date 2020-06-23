preco = float(input('Digite o valor do item: '))
quantidade = int(input('Digite a quantidade de produtos: '))

total = (preco * quantidade)

if total > 150:
    total = total * 0.9

print('O valor da compra foi: {}'.format(total))

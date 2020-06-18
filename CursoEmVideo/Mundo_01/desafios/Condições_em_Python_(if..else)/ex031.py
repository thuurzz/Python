# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Qual a distância da viagem em kms? '))
print('Corridas até 200km, valor: R$0.50 por km.')
print('Corridas acima de 200km, valor: R$0.40 por km.')

if distancia <= 200:
    print(f'O valor da corrida sera: R${distancia * 0.5 :.2f} ')
elif distancia > 200:
    print(f'O valor da corrida sera: R${distancia * 0.45 :.2f} ')

# Declaração do if em 1 linha
# preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45
# print(f'O valor sera {preco}')
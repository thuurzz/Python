# Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma
# mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Qual a velicidade do veículo: '))

limite = 80
excendente = velocidade - limite
valor_multa = excendente * 7

if velocidade > 80:
    print(f'Você foi multado pois ultrapassou o limimte de {limite}km/h!')
    print(f'A Multa sera no valor de: R${valor_multa:.2f}.')
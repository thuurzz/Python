# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu
# Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#
# – IMC abaixo de 18,5: Abaixo do Peso
#
# – Entre 18,5 e 25: Peso Ideal
#
# – 25 até 30: Sobrepeso
#
# – 30 até 40: Obesidade
#
# – Acima de 40: Obesidade Mórbida

print('=' * 30)
print('CALCULO DO IMC')
print('=' * 30)

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))


def calcula_imc(peso, altura):
    imc = peso / altura ** 2

    if imc < 18.5:
        status = 'Abaixo do peso.'
    elif imc >= 18.5 and imc <= 25:
        status = 'Peso ideal'
    elif imc > 25 and imc <= 30:
        status = 'Sobrepeso'
    elif imc > 30 and imc <= 40:
        status = 'Obesidade'
    else:
        status = 'Obesidade Mórbida'
    return status, imc


status, imc = calcula_imc(peso, altura)
print(f'Seu IMC é {imc:.1f} você esta na classificação: {status}')

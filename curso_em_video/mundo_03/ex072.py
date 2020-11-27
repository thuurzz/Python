#ex072

tup = 'zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze', 'dezesseis', 'dezessete','dezoito','dezenove','vinte'

n = int(input('Digite um número entre 0 e 20: '))
while not (n <= 20 and n >= 0):
    n = int(input('Tente novamente, digite um número entre 0 e 20: '))

print(f'Você digitou o número {tup[n]}.')
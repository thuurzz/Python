# Exercício Python 46: Faça um programa que mostre na tela
# uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.
import time
for i in range(10, -1, -1):
    print(i)
    time.sleep(0)
print('\033[7mzuuuuuuuuuuuuuuuuum', 13 * 'ta ', '\033[m')
print('\033[7mbuuuuum!\033[m')
print('\033[7mROJÃO 13 TIROS!\033[m')

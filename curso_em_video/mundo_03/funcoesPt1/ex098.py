'''
Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''
import time

def contador(inicio=0, final=0, passo=1):
    print('=' * 30)
    if passo == 0:
        print('Não é possível utilizar passo 0, será utilizado 1.')
        passo = 1
    elif passo < 0:
        passo *= -1

    print(f'Contagem de {inicio} até {final}, de {passo} em {passo}.')
    if inicio < final:
        for i in range(inicio, final+1, passo):
            print(i, end=' ', flush=True)
            time.sleep(0.5)
    else:
        for i in range(inicio, final-1, -passo):
            print(i, end=' ', flush=True)
            time.sleep(0.5) 
    print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)

while True:
    print('DIGITE VALORES PARA UMA CONTAGEM PERSONALIZADA')
    i = int(input('Digite o valor para iniciar a sequência: '))
    f = int(input('Digite o valor para finalizar a sequência: '))
    p = int(input('Digite o valor para o passo da sequência: '))
    contador(i, f, p)
    print()

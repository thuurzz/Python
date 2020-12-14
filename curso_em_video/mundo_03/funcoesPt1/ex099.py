# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
import cabecalho
import time


def maior(* num):
    """Função recebe vários números e mostra na tela a lista e o maior deles.
    """
    cabecalho.escreva('PROGRAMA MOSTRA MAIOR')
    maior = 0
    print(f'Analisando valores passados...')
    for i in range(len(num)):
        print(f'{num[i]}', end=' ', flush=True)
        time.sleep(0.3)
        if i == 0:
            maior = num[i]
        else:
            if num[i] > maior:
                maior = num[i]                 
    print(f'Foram passados {len(num)} valores ao todo.')
    print(f'O maior da lista é: {maior}.')
    cabecalho.escreva('FIM DO PROGRAMA')



maior(2, 9, 4, 5, 7, 1)

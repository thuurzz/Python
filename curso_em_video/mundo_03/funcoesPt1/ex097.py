'''
Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.                                  Ex:                                                escreva(‘Olá, Mundo!’) Saída:                                             
~~~~~~~~~
Olá,Mundo!                                             ~~~~~~~~~
'''

def escreva(frase):
    print('=' * (len(frase) + 4))
    print(f'  {frase}  ')
    print('=' * (len(frase) + 4))


escreva('Curso em vídeo de Python no YouTube')
escreva('Arthur Vinicius')
escreva('CeV')
escreva('PROGRAMA DE CALCULAR ÁREA')
escreva('FIM')


from datetime import date

# Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Digite o ano e sera exbido se é bissexto, ou digite 0 para analisar o ano atual. '))
if ano == 0:
    ano = date.today().year

if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano de {ano} é bissexto!')
else:
    print(f'Este ano {ano} não é bissexto!')
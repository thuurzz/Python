'''Exercício Python 114: Crie um código em Python que teste se o
site pudim está acessível pelo computador usado.'''

from ex114 import siteOn

site = input('Digite um site para verificar se está online: \033[;7m www.example.com \033[0;0m\n')
print(f'O site:\033[1;34m{site}\033[0;0m está: {siteOn(site)}')
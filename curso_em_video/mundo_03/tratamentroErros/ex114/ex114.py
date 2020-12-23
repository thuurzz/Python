'''Exercício Python 114: Crie um código em Python que teste se o
site pudim está acessível pelo computador usado.'''


def siteOn(site):
    import socket

    try:
        host = socket.gethostbyname(site)
        c = socket.create_connection((host, 80), 3)
        return '\033[1;32mOnline\033[0;0m'
    except:
        print("error")
    return '\033[1;31mOffline\033[0;0m'


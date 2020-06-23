#Arthur Vinicius Santos Silva RA:1903665

def eh_primo(n):
    res = False
    qdt_div = 0

    for i in range(1, n + 1):
        if (n % i) == 0:
            qdt_div += 1

    if qdt_div == 2:
        res = True
    return res


num = int(input('Digite um número: '))
primo = eh_primo(num)

if primo:
    print('{} é primo!'.format(num))
else:
    print('{} não é primo!'.format(num))

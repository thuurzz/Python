v = False #inicia flag booleano falso.
while not v: #enquanto a condição não for atendida, ou seja, se tone True, laço se repete.
    n = int(input('digite um número maior que 0: '))
    if n >= 0: #uma vez atendida, (v) recebe True, parando o laço.
        v = True

print(f'número {n} aceito!')

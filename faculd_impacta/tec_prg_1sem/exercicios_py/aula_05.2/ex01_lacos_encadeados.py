#tabuada do 0 a 10, de 0 a 10.
n = 1
while n <= 10: #varia (n) de 1 até 10_
    i = 0 #toda vez que a o laço se repete, (i) começa do 0:
    while i <= 10: #varia (i) de 0 até 10
        tab = i * n
        print(f'{n} x {i} = {tab}')
        i += 1
    print(20 * '=')
    n += 1

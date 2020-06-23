# Arthur Vincius Santos Silva RA1903665

n = int(input())
m = int(input())

if n > m:
    aux = n
    n = m
    m = aux

while n <= m:
    if (n % 2) == 1:
        print(n)
        n = n + 2
    else:
        n = n + 1

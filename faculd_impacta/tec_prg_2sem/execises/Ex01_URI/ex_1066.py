# URI 1066
par = impar = positivo = negativo = 0
for i in range(5):
    n = float(input())
    if n % 2 == 0:
        par += 1
    else:
        impar +=1
    if n > 0:
        positivo += 1
    elif n < 0:
        negativo +=1
print(f'''{par} valor(es) par(es)
{impar} valor(es) impar(es)
{positivo} valor(es) positivo(s)
{negativo} valor(es) negativo(s)''')

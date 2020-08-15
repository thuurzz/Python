# URI 1072

# Leia um valor inteiro N.
n = int(input())

# var de números dentro do intervalo [10,20]
dentro = fora = 0

# Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
for i in range(n):
    x = int(input())
    # se dentro do intervalo adiciona contador a var adequada
    if x >= 10 and x <= 20:
        dentro += 1
    else:
        fora +=1
print(f'''{dentro} in
{fora} out''')



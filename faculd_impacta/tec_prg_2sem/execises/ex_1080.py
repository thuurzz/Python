# URI Online Judge | 1080

# Leia 100 valores inteiros. 
maior = posicao = 0
# repete 100x a leitura de um inteiro
for i in range(100):
    n = int(input())
    # no primeiro loop, atribui os valores as var
    if i == 0:
        maior = n
        posicao = i + 1
    # se a entrada for maior que o já guardados, substitui na var
    if n > maior:
        maior = n
        posicao = i + 1
    # exibe resultados
print(f'{maior}\n{posicao}')
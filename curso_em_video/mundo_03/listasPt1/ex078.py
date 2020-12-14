#EX078

# lê valores e coloca na lista
valores = []
for i in range(5):
    n = int(input(f'Digite um valor para a Posição: {i+1}: '))
    valores.append(n)
print('=-' * 20)

# exibe lista
print(f'Você digitou os valores: {valores}')

# percorre lista e pega maior e menor
maior = menor = 0
for pos,num in enumerate(valores):
    if pos == 0:
        maior, posMaior = num, pos
        menor, posMenor = num, pos
    else:
        if num > maior:
            maior, posMaior = num, pos
        if num < menor:
            menor, posMenor = num, pos

# mostra maior
print(f'O maior valor digitado foi: {maior}, na posição: ', end='')
for p,v in enumerate(valores):
    if v == maior:
        print(f'{p}... ', end='')
print()

# mostra menor
print(f'O menor valor digitado foi: {menor}, na posição: ', end='')
for p,v in enumerate(valores):
    if v == menor:
        print(f'{p}... ', end='')
print()

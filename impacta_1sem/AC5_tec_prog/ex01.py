#Arthur Vinicius Santos Silva   RA:1903365
# Escreva a funcao todos_os_indices(seq, x) abaixo:
def todos_os_indices(seq, x):
    indices_de_x = [] #inicia a lista vazia
    for i in range(len(seq)): #repete len(seq) vezes
        if x == seq[i]: #se x esta na lista
            indices_de_x.append(i) #adicona o valor na lista
    return indices_de_x #retorna

# Programa principal (ja implementado, voce nao precisa se preocupar com o codigo partir deste ponto)
sequencia = eval(input())
valor = eval(input())
resultado = todos_os_indices(sequencia, valor)
if isinstance(resultado, list):
    if len(resultado) > 0:
        for item in resultado:
            print(item)
    else:
        print('lista vazia')
else:
    print('Erro. Voce deve devolver uma lista')

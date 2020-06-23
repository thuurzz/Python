# função que retorna a soma dos inteiros de 1 ate n.


def soma_1_ate_n(n): #cria a funcao
    soma = 0 #var acumuladora
    i = 1 #var contadora
    while i <= n: #laço de 1 até n
        soma = soma + i #rebe a soma de 1 até n
        i += 1 #incrementa o contador
    return soma #retorna a soma


n = int(input('Digite um numero inteiro: '))   #pede o inteiro
total = soma_1_ate_n(n) #atribui soma a var  total
print(f'A soma dos inteiros de 1 ate {n} é: {total}') #exibe total

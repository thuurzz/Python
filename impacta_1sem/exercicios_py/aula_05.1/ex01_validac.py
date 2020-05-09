num = int(input('digite um num entre 1 e 50: '))

while num <1 or num > 50: #caso não esteja dentro do intervalo, pede novo número.
    #a condição cima poderia ser descrita como: not (num => 1 and num <= 50)
    num = int(input('tente novamente: \n'))
print(f'Numero aceito! {num}')

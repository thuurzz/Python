#Arthur Vinicius Santos Silva RA:1903365

# Escreva o codigo da funcao le_e_devolve_menor() na sequencia:
def le_e_devolve_menor():
    cond = True
    n = int(input())
    if n >= 0:
        menor_ = n
    else:
        menor_ = 0

    while cond:
        if n < menor_ and n > 0:
            menor_ = n

        if n >= 0:
            cond = True
        else:
            cond = False

        if n >=0:
            n = int(input())

    return menor_


# Escreva o codigo da funcao le_e_devolve_maior() na sequencia:
def le_e_devolve_maior():
    maior_ = 0
    n = 0
    cond = True

    while cond:
        n = int(input())
        if n > maior_:
            maior_ = n

        if n >= 0:
            cond = True
        else:
            cond = False

    return maior_

# Programa principal (ja implementado, voce nao precisa se preocupar com o codigo a partir deste ponto)
opcao = input()
if opcao == 'menor':
    menor = le_e_devolve_menor()
    print(menor)
elif opcao == 'maior':
    maior = le_e_devolve_maior()
    print(maior)

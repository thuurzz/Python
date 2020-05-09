#Arthur Vinicius Santos Silva RA:1903365

# Escreva o codigo da funcao le_e_devolve_menor() na sequencia:
def le_e_devolve_menor():
    n = int(input())
    if n >= 0:
        menor = n
    else:
        menor = 0

    while True:
        if n < menor and n > 0:
            menor = n

        if n < 0:
            break

        n = int(input())

    return menor


# Escreva o codigo da funcao le_e_devolve_maior() na sequencia:
def le_e_devolve_maior():
    n = int(input())
    if n >= 0:
        maior = n
    else:
        maior = 0

    while True:
        if n > 0:
            maior = n
        else:
            break

        n = int(input())

    return maior

# Programa principal (ja implementado, voce nao precisa se preocupar com o codigo a partir deste ponto)
opcao = input()
if opcao == 'menor':
    menor = le_e_devolve_menor()
    print(menor)
elif opcao == 'maior':
    maior = le_e_devolve_maior()
    print(maior)

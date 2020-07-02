# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

maior = menor = media = soma = div_media = 0  # inicia as var em 0
i = 1  # inicia o contador em 1 para ser != de 0 no while
while i != 0:
    n = int(input('Digite um número: '))  # pede o número
    if n != 0:  # se o número digitado for diferente de 0

        # soma valores á média, soma contador para divisão posterior
        soma += n  # adiciona valor a soma
        div_media += 1  # adiciona 1 ao contador que sera o divisor da média

        # verifica maior e menor digitados
        if i == 1:
            maior = menor = n
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        i += 1  # +1 ao contador/flag

    # Pergunta ao usuário se quer continuar
    opc = input('Deseja adicionar mais um número: [S]/[N]: ').strip().upper()[0]
    if opc == 'N':
        i = 0


# mostra a média
media = soma / div_media
print(f'A média de todos os valores digitados é: {media}')

# mostra qual maior e menor
print(f'O maior valor digitado foi: {maior} e o menor valor foi: {menor}.')


# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# média de idade do grupo
# qual é o nome do homem mais velho
# quantas mulheres têm menos de 20 anos.

media_idades = 0
idade_velho = 0
nome_velho= ''
qtd_mulheres = 0


for i in range(4):
    print('=' * 30)
    print(f'{i + 1}º PESSOA')
    nome = input('Qual seu nome: ').strip()
    idade = int(input('Qual sua idade: '))
    sexo = input('Sexo: [M] ou [F]:').upper()
    
    # recebe as idades e soma
    media_idades += idade
    
    # verifica se é o homem mais velho e guarda o nome
    if idade > idade_velho and sexo == 'M':
        nome_velho = nome
        idade_velho = idade
        
    # conta quantidade de mulheres com menos de 20 anos
    if sexo == 'F' and idade < 20:
        qtd_mulheres += 1
     
# divide a soma das idades por 4   
media_idades /= 4

print(f'A média das idades é: {media_idades}.')
print(f'O homem mais velho se chama: {nome}.')
print(f'Nesse grupo tem {qtd_mulheres} mulheres com menos de 20 anos.')

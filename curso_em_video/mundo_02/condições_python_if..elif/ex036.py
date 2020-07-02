import time

# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print(50 * '=')
print('PROGRAMA DE ANALISE DE FINANCIAMENTO')
print(50 * '=')

print('Digite o valor do seu salario, valor imóvel a ser financiado e tempo de financiamento, após analise serão '
      'exibidas condições do financiamento.')

valor_imovel = float(input('Digite o valor do imóvel a ser financiado: R$')) # receve valor do imóvel
salario = float(input('Digite o valor do seu salario: R$')) # recebe valor salário
anos_financ = int(input('Digite em quantos anos pretende financiar: ')) # recebbe quantidade de anos a financiar
meses_financ = anos_financ * 12 # transforma anos em meses
print('PROCESSANDO...')
time.sleep(2)
print(50 * '=')

valor_parc = valor_imovel / meses_financ #define valor da parcela

aprovado = valor_parc < (salario * (30/100)) # se menor que 30% so salário, aprova

reprovado = valor_parc > (salario * (30/100)) # se maior que 30% so salário, repoprova

if aprovado:
    print('\033[1;7mSeu financiamento foi aprovado!\033[m')
else:
    print('\033[1;7mInfelizmente seu financiamento não foi aprovado, tente novamente com novas condições.\033[m')
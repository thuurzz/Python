import time

print(50 * '=')
print('PROGRAMA DE ANALISE DE FINANCIAMENTO')
print(50 * '=')

print('Digite o valor do seu salario, valor imóvel a ser financiado e tempo de financiamento, após analise serão '
      'exibidas condições do financiamento.')

salario = float(input('Digite o valor do seu salario: '))
valor_imovel = float(input('Digite o valor do imóvel a ser financiado: '))
anos_financ = int(input('Digite em quantos anos pretende financiar: '))
meses_financ = anos_financ * 12
print('PROCESSANDO...')
time.sleep(2)
print(50 * '=')

valor_parc = valor_imovel / meses_financ

aprovado = valor_parc < (salario * (30/100))

reprovado = valor_parc > (salario * (30/100))

if aprovado:
    print('\033[1;7mSeu financiamento foi aprovado!\033[m')
else:
    print('\033[1;7mInfelizmente seu financiamento não foi aprovado, tente novamente com novas condições.\033[m')
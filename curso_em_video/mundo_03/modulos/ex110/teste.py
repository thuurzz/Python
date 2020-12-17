import moeda

# Programa principal
p = float(input('Digite o valor R$: '))
txa = float(input('Digite o valor da taxa para aumento: '))
txd = float(input('Digite o valor da taxa para aumento: '))
moeda.resumo(valor=p,vAumento=txa, vDecresc=txd)
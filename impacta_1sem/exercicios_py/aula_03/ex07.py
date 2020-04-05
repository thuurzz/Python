#Dado o preço de um produto (inteiro), elabore um programa que calcule e apresente a menor
#quantidade de notas (de cada valor) necessárias para efetuar o pagamento da compra desse
#produto. Considere como valores das notas atuais: 1, 2, 5, 10, 20, 50, 100.

v_prod = int(input('Digite o valor de um determinado produto sem casas decimais: '))

nota_100 = v_prod // 100
v_prod = v_prod - (100 * nota_100)

nota_50 = v_prod // 50
v_prod = v_prod - (50 * nota_50)

nota_20 = v_prod // 20
v_prod = v_prod - (20 * nota_20)

nota_10 = v_prod // 10
v_prod = v_prod - (10 * nota_10)

nota_5 = v_prod // 5
v_prod = v_prod - (5 * nota_5)

nota_2 = v_prod // 2
v_prod = v_prod - (2 * nota_2)

nota_1 = v_prod // 1
v_prod = v_prod - (1 * nota_1)

print('Para o valor de: {} R$.'.format(v_prod))
print('Serão necessárias: {} notas de 100 R$'.format(nota_100))
print('Serão necessárias: {} notas de 50 R$'.format(nota_50))
print('Serão necessárias: {} notas de 20 R$'.format(nota_20))
print('Serão necessárias: {} notas de 10 R$'.format(nota_10))
print('Serão necessárias: {} notas de 5 R$'.format(nota_5))
print('Serão necessárias: {} notas de 2 R$'.format(nota_2))
print('Serão necessárias: {} notas de 1 R$'.format(nota_1))

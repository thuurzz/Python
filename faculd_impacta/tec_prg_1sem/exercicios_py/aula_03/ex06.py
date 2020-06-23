'''
Faça um programa que receba o custo de um espetáculo teatral e o preço do convite desse
espetáculo. Esse programa deve calcular e mostrar:
a) A quantidade de convites que devem ser vendidos para que pelo menos o custo do
espetáculo seja alcançado.
b) A quantidade de convites que devem ser vendidos para que se tenha um lucro de 23%.
'''

c_esp = float(input('Digite o valor do custo do espetáculo: '))
p_con = float(input('Digite o valor do custo do convite: '))

conv_qtd = round((c_esp / p_con))
lucro23 = round(((c_esp + ((c_esp) * (23/100))) / p_con)+0.5)

print('Para que o custo do espetáculo seja coberto, serão necessários: {} convites.'.format(conv_qtd))
print('Para que o custo do espetáculo seja coberto e haja um lucro de 23% serão necessários: {} convites.'.format(lucro23))

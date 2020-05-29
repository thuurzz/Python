salario_bruto = float(input())
tempo_relacionamento = int(input())
valor_emprestimo = float(input())

if salario_bruto > 2350: # primeiro if
    if tempo_relacionamento >= 5: #segundo if
        juros = valor_emprestimo * 0.10
    elif tempo_relacionamento >= 2 and tempo_relacionamento < 5: #elif
        juros = valor_emprestimo * 0.15
    else:
        juros = valor_emprestimo * 0.20
    print('O valor do juros é: ', juros)
else:
    print('Empréstimo negado')

'''
Resposta:
if salario_bruto > 2350: # primeiro if
if tempo_relacionamento >= 5: #segundo if
elif tempo_relacionamento >= 2 and tempo_relacionamento < 5: #elif

'''

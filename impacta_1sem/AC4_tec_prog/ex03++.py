import sys
# Escreva o codigo da funcao le_e_devolve_menor() na sequencia:
#Arthur Vinicius Santos Silva RA:1903365
def le_e_devolve_menor():
	m = sys.maxsize
	while True:
		n = int(input())
		if n < 0:
			break
		else:
			if n >=0 and n < m:
				m = n
	if m == sys.maxsize:
		m = 0
	return m
    

# Escreva o codigo da funcao le_e_devolve_maior() na sequencia:
#Arthur Vinicius Santos Silva RA:1903365
def le_e_devolve_maior():
	m = 0
	while True:
		n = int(input())
		if n < 0:
			break
		else:
			if n > m:
				m = n
	return m

# Programa principal (ja implementado, voce nao precisa se preocupar com o codigo a partir deste ponto)
opcao = input()
if opcao == 'menor':
	menor = le_e_devolve_menor()
	print(menor)
elif opcao == 'maior':
	maior = le_e_devolve_maior()
	print(maior)
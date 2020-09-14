# URI Online Judge | 1140

# receberá valor N ou Y para tautograma
isTau = 0

# repete teste até entrar com '*'
while True:
	# se '*' para programa
	frases = input().split()
	if frases[0][0] == '*':
		break
	
	# itera lista frases
	for letra in range(len(frases)):
		# se a prim letra da prim palavra igual das outras, Y.
		if frases[0][0].lower() == frases[letra][0].lower():
			isTau = 'Y' 
		# se diferente, N e para de verificar
		elif  frases[0][0].lower() != frases[letra][0].lower():
			isTau = 'N'
			break
	# exibe resultado
	print(isTau)
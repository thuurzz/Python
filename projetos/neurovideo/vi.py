import time

# Pede o nome
nome = input('Qual seu nome? ').strip().upper()[0]
while not nome == 'V':
    nome = input('Talvez não seja quem estou procurando, vamos tentar de novo. Qual seu nome? ').strip().upper()[0]

print('=' * 20)
print('Processando...')
print('=' * 20)
time.sleep(1)

# apresentação, primeira dica
print('Olá Virgínia, como foi sua noite?')
print('Vamos jogar um jogo?')
print('Nível 1')
print('Seu agrado esta escondido em algum lugar deste setor, mas onde?')
time.sleep(5)
print('Quem sabe no armário do Manitol...')
time.sleep(5)

# pede primeiro código
c1 = input('Encontrou algo, o que esta escrito? ').strip().upper()
while not c1 == 'ENCANTADORA':
    c1 = input('Gostaria de tentar de novo? ').strip().upper()

# segunda dica
print('=' * 20)
print('Processando...')
print('=' * 20)
time.sleep(2)
print('Humm.. código aceito, acho que você despertou a curiosade de alguém.\n')
time.sleep(1)
print('Nível 2')
print('Próxima dica: ')
print('Vejamos se encotra algo... na porta do armário de roupas que fica no corredor.')
time.sleep(5)

# pede segundo código
c2 = input('Encontrou algo, o que esta escrito? ').strip().upper()
while not c2 == 'OLHOS LINDOS':
    c2 = input('Gostaria de tentar de novo? ').strip().upper()

# segunda dica
print('=' * 20)
print('Processando...')
print('=' * 20)
time.sleep(2)
print('Humm.. código aceito, acho que alguém gostou dos seus olhos.\n')
time.sleep(1)
print('Nível 3')
print('Ultima dica: ')
print('Após essa volta toda, talvez encontre algo...\n'
      'De baixo deste teclado que esta com as mãos agora.')
time.sleep(5)

# pede terceiro código
c3 = input('O que esta escrito? ').strip().upper()
while not c3 == 'BORBOLETAS':
    c3 = input('Gostaria de tentar de novo? ').strip().upper()

# mostra local recompensa
print('=' * 20)
print('Processando...')
print('=' * 20)
time.sleep(3)
print('Parece que alguém fica com borboletas no estômago quando esta perto de você,\n'
      'mas aparentemente tem alguém lendo essa mensagem que se sente assim também...\n')
time.sleep(5)
print('=' * 20)
print('FIM DE JOGO...')
print('=' * 20)
print('\033[;7mCONQUISTA DESBLOQUEADA: Sorriso bobo +5\033[m\n')
print('\033[;7mVocê cumpriu todos os objetivos, passe a mão em baixo da mesa e terá sua recompensa.\033[m')








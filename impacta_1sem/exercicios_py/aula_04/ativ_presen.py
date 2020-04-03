# Arthur Vinicius Santos Silva  RA:1903665
'''
1) Crie um programa em Python que leia a nota e a quantidade de faltas de um aluno.
Em seguida, crie uma função chamada exibe_status(n_aluno, f_aluno), onde os parâmetros
n_aluno e f_aluno representam a nota e a quantidade de faltas de um determinado aluno. Seu
programa principal deve chamar essa função e passar os valores lidos por parâmetro.
a) Dentro da função construa a seguinte lógica:
1. Se n_aluno for maior ou igual a 7.0 e f_aluno for menor ou igual a 25, exibe a mensagem:
Aluno aprovado!
2. Se n_aluno for maior ou igual a 5.0 e f_aluno for menor ou igual a 25, exibe a mensagem:
Aluno em recuperação!
3. Caso contrário exiba a mensagem: Aluno reprovado!
b) Usando os operadores relacionais e lógicos aprendidos na última aula (aula 4) qual seria a
expressão lógica que representaria o caso contrário. Isto é, se você tivesse que fazer um if para
testar se o aluno foi reprovado, qual seria a condição lógica deste if?
(Coloque a resposta b) dentro do seu código como comentário).
'''

def exibe_status(n_aluno, f_aluno):
    print('Voce teve: {} faltas.\nSua nota foi: {}.'.format(f_aluno, n_aluno))
    if (n_aluno >= 7.0) and (f_aluno <= 25):
        print('Aluno aprovado!') 
    elif (n_aluno >= 5.0) and (f_aluno <= 25):
        print('Aluno em recuperação!')
    else:
        print('Aluno reprovado!')

nota = float(input('Digite sua nota: '))
falta = int(input('Digite a quantidade de faltas: '))

exibe_status(nota, falta)

#b) if (nota < 5) or (falta > 25):
#       print('Aluno reprovado!')


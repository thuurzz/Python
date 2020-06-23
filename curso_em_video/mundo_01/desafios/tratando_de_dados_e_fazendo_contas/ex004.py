algo = input('Digite algo:')

print('o tipo primitivo desse valor é:', type(algo))
print('só tem espaços?', algo.isspace())
print('é um número?', algo.isalnum())
print('é alfabético?', algo.isalpha())
print('é alfanumérico?', algo.isalnum())
print('esta em minúscula?', algo.isupper())
print('esta em minúsculo?', algo.islower())

print('esta capitalizada? {}'.format(algo.istitle()))

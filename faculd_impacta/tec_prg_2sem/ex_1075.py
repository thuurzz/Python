# URI Online Judge | 1075

# Leia um valor inteiro N
n = int(input())

#Apresente todos os números entre 1 e 10000 
# que divididos por N dão resto igual a 2.

for i in range(1,10001):
    if i % n == 2:
        print(i)
# lê numero inteiro
# n = int(input('Digite um número: '))

n = 10
i = 0
fb_n = 1
seq_fb = []
while i < n:
    fb_n = i + fb_n
    seq_fb.append(fb_n)
    i += fb_n
    # print(f'O {i}º temro da seqência Fibonacci é: ')
print(seq_fb)

# REVISAR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

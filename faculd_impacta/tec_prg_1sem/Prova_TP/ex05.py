#fazer a condição para o if funcionar

media_provas = float(input())
media_trabalhos = float(input())
qtd_faltas = int(input())

if (media_provas >= 6) and (media_trabalhos >= 5) and (qtd_faltas < 8):
    print('aprovado')
else:
    print('reprovado')

# resp: (media_provas >= 6) and (media_trabalhos >= 5) and (qtd_faltas < 8)

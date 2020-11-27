# ex073

brasileiro = ('Atletico-MG', 'Flamengo', 'São Paulo', 'Internacional',
'Fluminense','Palmeiras','Santos','Grêmio','Corinthians','Athletico-PR',
'Bahia','Fortaleza','Bragantino','Ceará SC','Sport Recife','Vasco da Gama','Coritiba','Botafogo','Goiás','Chapecoense')

# A) 5 PRIMEIROS COLOCADOS
print(f'5 PRIMEIROS COLOCADOS:{", ".join(brasileiro[:5])}.')
print('=' * 20)
# B) OS 4 ÚLTIMOS COLOCADOS
print(f'OS 4 ÚLTIMOS COLOCADOS:{", ".join(brasileiro[-4:])}.')
print('=' * 20)
# C) TIMES EM ORDEM ALFABÉTICA
print(f'TIMES EM ORDEM ALFABÉTICA:{", ".join(sorted(brasileiro))}.')
print('=' * 20)
# D) QUAL POSIÇÃO DO CHAPECOENCE
print(f'POSIÇÃO DO CHAPECOENCE:{brasileiro.index("Chapecoense")}.')
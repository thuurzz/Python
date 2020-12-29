usuarios = {}
usuarios = {
    "Chaves": ["Chaves Silva", "17/06/1975", "Recep_01"],
    "Quico": ["Enrico Flores", "03/06/1976", "Raiox_03"],
    "Florinda": ["Florinda Flores", "26/11/2016", "Recep_01"]
}

print(usuarios)
print('=' * 20)
for k, v in usuarios.items():
    print(f'{k} {v}')

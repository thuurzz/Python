nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

# PRIMEIRO PROBLEMA A SER RESOLVIDO
while True:
    doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa? [SIM]/[NAO] ").upper()
    if doenca_infectocontagiosa in ('SIM', 'NAO'):
        break

if doenca_infectocontagiosa == "SIM":
    print("Encaminhe o paciente para sala AMARELA")
else:
    print("Encaminhe o paciente para sala BRANCA")

# SEGUNDO PROBLEMA A SER RESOLVIDO
if idade >= 65:
    print("Paciente COM prioridade")
else:
    genero = input("Digite o gênero do paciente: ").upper()
    if genero == "FEMININO" and idade > 10:
        gravidez = input("A paciente está grávida? ").upper()
        if gravidez == "SIM":
            print("Paciente COM prioridade")
        else:
            print("Paciente SEM prioridade")
    else:
        print("Paciente SEM prioridade")

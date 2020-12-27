"""
Procure criar um arquivo chamado DesafioDecisao.py e elaborar o código para resolver a seguinte situação: o seu módulo solicitará o nível de acesso de uma pessoa que pode ser: ADM, USR ou GUEST e o gênero dessa pessoa, caso o nível seja ADM, ele deverá exibir “Olá administrador” para os homens ou “Olá administradora” para as mulheres. Se o nível for USR, deverá exibir “Olá usuário” para os homens ou “Olá usuária” para as mulheres. Se o nível for GUEST, a mensagem deverá ser “Olá visitante”. E se o nível digitado for diferente de ADM, USR ou GUEST deverá exibir a mensagem “Olá desconhecido(a)”.
"""

nv = input('Selecione seu nível de acesso ao sistema [ADM]/[USR]/[GUEST]: ').upper()
if nv == 'ADM' or nv == 'USR':
    genero = input('Genêro [M]/[F]: ').upper()[0]
    if genero == 'ADM':
        if genero == 'F':
            print('Olá administradora')
        else:
            print('Olá administrador')
    else:
        if genero == 'F':
            print('Olá usuária')
        else:
            print('Olá usuário')
elif nv == 'GUEST':
    print('Olá visitante')
else:
    print('Olá desconhecido(a)')
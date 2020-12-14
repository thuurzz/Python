class Pessoa:
    
    def __init__(self, nome):
        self.nome = nome

    def apresenta(self):
        print('Oi eu sou o ' + self.nome)

joao = Pessoa('joao')
maria = Pessoa('maria')

joao.apresenta()
print(joao.nome)
maria.apresenta()
print(maria.nome)
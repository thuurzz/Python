# Arthur Vincius Santos Silva RA1903665
class AchaImpar:
    def __init__(self,n ,m):
        self.n = n
        self.m = m
        self.aux = 0
        self.n_maior = self.n > self.m #verifica se n é maior que m


    def inverte_var(self): #função pra inverter se for maior
        if self.n_maior:
            self.aux = self.n
            self.n = self.m
            self.m = self.aux


    def imprime_valor(self): #imprime valor impar
        while self.n <= self.m:
            if (self.n % 2) == 1:
                print(self.n)
                self.n = self.n + 2
            else:
                self.n = self.n + 1



if __name__ == '__main__':
    n = int(input()) #lê o primeiro
    m = int(input()) #lê o segundo

    acha_impar = AchaImpar(n, m)
    acha_impar.inverte_var()
    acha_impar.imprime_valor()





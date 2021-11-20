import random


class ChuteONumero:
    def __init__(self):
        self.valorAleatorio = 0
        self.valorMinimo = 1
        self.valorMaximo = 100
        self.tentarNovamente = True

    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        try:
            while self.tentarNovamente == True:
                if int(self.valorDoChute) > self.valorAleatorio:
                    print('Chute um valor menor')
                    self.PedirValorAleatorio()
                elif int(self.valorDoChute) < self.valorAleatorio:
                    print('Chute um valor maior')
                    self.PedirValorAleatorio()
                if int(self.valorDoChute) == self.valorAleatorio:
                    print('PARABÉNS VOCÊ ACERTOU!')
                    break
        except:
            print('Por favor, digitar apenas números!')
            self.Iniciar()

    def PedirValorAleatorio(self):
        self.valorDoChute = input('Chute um valor: ')

    def GerarNumeroAleatorio(self):
        self.valorAleatorio = random.randint(self.valorMinimo, self.valorMaximo)

chute = ChuteONumero()
chute.Iniciar()
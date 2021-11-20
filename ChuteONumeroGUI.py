import random
import PySimpleGUI as sg


class ChuteONumero:
    def __init__(self):
        self.valorAleatorio = 0
        self.valorMinimo = 1
        self.valorMaximo = 100
        self.tentarNovamente = True

    def Iniciar(self):
        #layout
        layout = [
            [sg.Text('Seu Chute:', size=(39,0))],
            [sg.Input(size=(18,0), key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(39,10))]
        ]
        #criar uma janela
        self.janela = sg.Window('Chute o numero!', layout=layout)
        self.GerarNumeroAleatorio()
        try:
            while True:
                #receber os valores
                self.evento, self.valores = self.janela.Read()
                #fazer algo com os valores
                if self.evento == 'Chutar!':
                    self.valorDoChute = self.valores['ValorChute']
                    while self.tentarNovamente == True:
                        if int(self.valorDoChute) > self.valorAleatorio:
                            print('Chute um valor menor')
                            break
                        elif int(self.valorDoChute) < self.valorAleatorio:
                            print('Chute um valor maior')
                            break
                        if int(self.valorDoChute) == self.valorAleatorio:
                            self.tentarNovamente = False
                            print('PARABÉNS VOCÊ ACERTOU!')
                            break
        except:
            print('Por favor, digitar apenas números!')
            self.Iniciar()

    def LerValorDaTela(self):
        self.evento, self.valores = self.janela.Read()

    def GerarNumeroAleatorio(self):
        self.valorAleatorio = random.randint(self.valorMinimo, self.valorMaximo)

chute = ChuteONumero()
chute.Iniciar()
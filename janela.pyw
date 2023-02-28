from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ('Arial', '10')
        self.primeiroContainer = Frame(master)
        self.primeiroContainer['pady'] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer['padx'] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer['padx'] = 20
        self.segundoContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer['padx'] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer['padx'] = 20
        self.quintoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text='Cálculo de Salário', fg='blue')
        self.titulo['font'] = ('Arial', '10', 'bold')
        self.titulo.pack(side=LEFT)

        self.pontos = Label(self.segundoContainer, text='Pontos', font=self.fontePadrao, fg='blue')
        self.pontos.pack(side=LEFT)

        self.pontos = Entry(self.segundoContainer)
        self.pontos['width'] = 30
        self.pontos['font'] = self.fontePadrao
        self.pontos.pack(side=LEFT)

        self.sal = Label(self.quintoContainer, text='Valor Bruto:', font=self.fontePadrao, fg='blue')
        self.sal.pack(side=LEFT)

        self.A = Button(self.quartoContainer)
        self.A['text'] = 'A'
        self.A['font'] = ('Calibri', '8')
        self.A['width'] = 13
        self.A['command'] = self.calA
        self.A.pack(side=LEFT)

        self.B = Button(self.quartoContainer)
        self.B['text'] = 'B'
        self.B['font'] = ('Calibri', '8')
        self.B['width'] = 13
        self.B['command'] = self.calB
        self.B.pack(side=LEFT)

        self.C = Button(self.quartoContainer)
        self.C['text'] = 'C'
        self.C['font'] = ('Calibri', '8')
        self.C['width'] = 13
        self.C['command'] = self.calC
        self.C.pack(side=LEFT)

        self.mensagem = Label(self.quintoContainer, text='', font=self.fontePadrao)
        self.mensagem.pack(side=LEFT)

        #Método verificar pontos
    def calA(self):
        ponto = float(self.pontos.get())
        somaPont = (ponto * 0.135804) + 1650
        self.mensagem['text'] = (f'{somaPont:.2f}')
    def calB(self):
        ponto = float(self.pontos.get())
        somaPont = (ponto * 0.135804) + 1060
        self.mensagem['text'] = (f'{somaPont:.2f}')
    def calC(self):
        ponto = float(self.pontos.get())
        somaPont = (ponto * 0.135804 + 750)
        self.mensagem['text'] = (f'{somaPont:.2f}')

root = Tk()
Application(root)
root.mainloop()

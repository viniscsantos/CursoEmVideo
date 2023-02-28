from tkinter import *
class Janela:
    def __init__(self, toplevel):
        self.fr1 = Frame(toplevel)
        self.fr1.pack()

        self.msg = Label(self.fr1, text='Cálculo de Salário')
        self.msg.pack()

        self.botao1 = Button(self.fr1, text='A')
        self.botao1['background'] = 'gray'
        self.botao1['fg'] = 'red'
        self.botao1['font'] = ('italic', '30')
        self.botao1.pack(side=LEFT)

        self.botao2 = Button(self.fr1, text='B')
        self.botao2['font'] = ('italic', '30')
        self.botao2['bg'] = 'gray'
        self.botao2['fg'] = 'red'
        self.botao2.pack()



raiz = Tk()
Janela(raiz)
raiz.mainloop()
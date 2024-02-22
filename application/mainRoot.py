from tkinter import *
from tkinter import ttk
from transition import Transition


class MainRoot():
    '''Classe que cria a tela principal e seus Widgets iniciais.'''
    def __init__(self) -> None:
        self.root = Tk()
        self.root.geometry('500x100')
        self.root.title('Cotações')
        self.root.iconbitmap('icon/icon.ico')
        self.root.resizable(False, False)
        self.createHeader()
        self.obj_transition = Transition(self.root, self.content, self.btnExibir, self.lblTitle)

    def createHeader(self):
        '''Cria o cabeçalho da interface.'''
        # frame pai denomicontent para organizar todos os outros widgets da interface
        self.content = Frame(self.root)
        self.content.grid(column=0, row=0) # posicionado na coluna 0 da linha 0
        
        self.createTitle()
        self.createButton()
        
    def createTitle(self):
        '''Cria e estiliza o títuo da interface.'''
        # frame que define o bg de onde ficará a label do título
        self.frameTitle = Frame(self.content, borderwidth=3, relief='ridge', width=500, height=50, bg='black')
        # neste ponto, a grade possui 3 linhas(0, 1, 2) e 3 colunas (0, 1, 2)
        self.frameTitle.grid(row=0, column=0, rowspan=3, columnspan=3) # faz o frame ocupar 3 linhas e 3 colunas da geometria da tela
        # label do título principal da interface
        self.lblTitle = Label(self.content, text='Cotações das Moedas', bg = 'black', foreground='white', font='arial 15')
        self.lblTitle.grid(row=1, column=1) # ocupa a linha 1 e a coluna 1, posicionando-o no centro da frameTitle
        
    def createButton(self):
        '''Cria o botão principal da interface.'''
        # frame utilizado para posicionar o button centralizado 
        self.frameButton = Frame(self.content, width=500, height=50)
        # neste ponto, a grade possui 4 linhas (0, 1, 2, 3) ainda 3 colunas
        self.frameButton.grid(row = 3, columnspan=3) # o frame ficará posicionado na quarta linha (index 3) e ocupará 3 colunas 
        self.btnExibir = Button(self.content, text='Exibir Cotas', width=15, command=lambda: self.obj_transition.createQuotes())
        self.btnExibir.grid(row=3, column=1)
        
    def updateScreen(self):
        '''Mantém a tela ativa e a atualiza.'''
        self.root.mainloop()


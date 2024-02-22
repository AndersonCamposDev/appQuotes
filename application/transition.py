from tkinter import *
from tkinter import ttk
from quotes import Quotes

class Transition:
    '''Classe responsável por realizar todas as transições da tela
    criação de botões auxiliares, exclusão e criação de widgets, etc.'''
    def __init__(self, root, content, btnExibir, lblTitle) -> None:
        '''Inicializa os atributos da classe que foram passados através do método construtor
        da classe Tela'''
        self.root = root
        self.content = content
        self.btnExibir = btnExibir
        self.lblTitle = lblTitle
        # atributo que cria um objeto da classe Quotes, que faz a requisição da API e obtém os valores 
        self.quotes = Quotes()

    def createQuotes(self):
        '''Cria a exibição inicial da cotas, expande a tela, desativa respectivo botão,
        além dos botões auxiliares de Legenda e Conversão.'''
        # cria um frame auxiliar onde serão posicionados todos os widgets criados a partir daqui
        frameAux = Frame(self.content, width=500, height=350)
        frameAux.grid(row=4, rowspan=3, columnspan=3)
        
        
        self.root.geometry('500x450')
        self.createLabelQuotes(frameAux)
        self.btnExibir['state'] = 'disabled'
        self.createAUXButtons(frameAux)
        self.lblTitle['text'] = 'Cotação das moedas'

    def createLabelQuotes(self, frameAux):
        '''Exibe o valor de todas as cotas obtidas a partir da requisição feita à API'''
        self.cleanerScreen(frameAux)

        x_place= 10
        y_place= 5
        i = 0
        #Laço que percorre a lista com as informações de todas as cotas
        for dictionary in self.quotes.quotesList:
            
            if (i%3 == 0):
                x_place = 10
                y_place += 50
            
        
            lblText = f"{dictionary['code']}/{dictionary['codein']} - R$ {dictionary['bid']}"
            label = Label(frameAux, text=lblText, font='arial 9')
            label.place(x=x_place, y=y_place)
            
            i+=1
            x_place+=185
        
    def createAUXButtons(self, frameAux):
        '''Cria os botões auxiliares de exibir Legenda e criar o Conversor.'''
        btnConversor = Button(self.content, text='Converter', command=lambda: self.createConversor(frameAux, btnLegenda, btnConversor))
        btnConversor.grid(row=3, column=0)
        btnLegenda = Button(self.content, text='Legenda', command=lambda: self.createSubtitles(frameAux, btnLegenda, btnConversor))
        btnLegenda.grid(row=3, column=2)

    def createSubtitles(self, frameAux, btnLegenda, btnConversor):
        '''Cria as legendas, muda o título da aplicação, desativa o respectivo botão disponibiliza os outros.'''
        self.lblTitle['text'] = 'Legendas'
        btnLegenda['state'] = 'disabled'
        self.btnExibir['state'] = 'normal'
        btnConversor['state'] = 'normal'
        
        self.cleanerScreen(frameAux)
        
        x_place= 2
        y_place= 5
        i = 0
        # laço que percore a lista com as informações de todas as cotas, dessa vez obtendo o código e o nome da respectiva moeda 
        for dictionary in self.quotes.quotesList:
            
            if (i%3 == 0):
                x_place = 2
                y_place += 50
            
            lblText = f"{dictionary['code']} - {dictionary['name']}"
            label = Label(frameAux, text=lblText, font='arial 9')
            label.place(x=x_place, y=y_place)
            
            i+=1
            x_place+=175

    def createConversor(self, frameAux, btnLegenda, btnConversor):
        '''Cria o conversor, muda o título da aplicação, desativa o respectivo botão e dispobibiliza os outros. '''
        self.lblTitle['text'] = 'Conversor'
        btnLegenda['state'] = 'normal'
        self.btnExibir['state'] = 'normal'
        btnConversor['state'] = 'disabled'

        self.cleanerScreen(frameAux)

        names = []
        # obtém o nome de todas as moedas para criar a legenda da Combobox
        for dictionary in self.quotes.quotesList:
            names.append(f"{dictionary['name']}")

        self.createConversorScreen(frameAux, names)
   
    def createConversorScreen(self, frameAux, names):
            '''Cria todos os widgets referentes à opção de conversão de moedas (Labels, Combobox, Entry e Buttons.)'''
            subtitle = Label(frameAux, text='Selecione a moeda desejada : ', font='Arial 10')
            subtitle.place(x=40, y=20)

            quoteChoosen = ttk.Combobox(frameAux, values=names, width=25)
            quoteChoosen.current(0)
            quoteChoosen.place(x=220, y=20)
            
            lblValor = Label(frameAux, text='Valor : ', font='Arial 10')
            lblValor.place(x=175, y=70)
            
            entry = Entry(frameAux, bd=3)
            entry.insert(0, '0')
            entry.place(x=220, y=70)

            exemplo = Label(frameAux, text='(Ex: 1.25; 10.50; 20)', font='Arial 8', foreground='gray')
            exemplo.place(x=350, y=70)

            btnConverter = Button(frameAux, text='Converter', command=lambda: self.converter(entry, quoteChoosen, frameAux, btnConverter))
            btnConverter.place(x=220, y=120)
    
    def converter(self, entry, quoteChoosen, frameAux, btnConverter):
        '''Converte o valor da entrada da moeda selecionada para BRL.'''
        btnConverter['state'] = 'disabled'
        
        # obtém o valor de entrada e o país de origem
        value = float(entry.get())
        moeda = quoteChoosen.get()

        # label para exibir o resultado 
        lblConversao = Label(frameAux, font='Arial 11')
        lblConversao.place(x=40, y=180)

        for dictionary in self.quotes.quotesList:
            if (dictionary['name'] == moeda):
                code = dictionary['code'] # obtém o cód. da moeda selecionada e o valor da moeda 
                bid = dictionary['bid']
        
        if (value <= 0): # caso o valor informado seja inválido
            lblConversao['text'] = 'Valor Inválido, tente novamente.'
        
        else:
            # caso o resultado seja válido
            lblConversao['text'] = f'{code} {value} = R$ {round(value*bid, 2)}'
            
        btnLimpar = Button(frameAux, text='Limpar', command=lambda: self.limparResultado(lblConversao, btnLimpar, btnConverter))
        btnLimpar.place(x=220, y=210)


    def cleanerScreen(self, frameAux):
        '''Limpa todos os widgets da tela sempre que um botão é ativado, 
        para os novos widgets serem posicionados corretamente.'''
        
        wigets = frameAux.place_slaves() 
        for widget in wigets:
            widget.destroy()

    def limparResultado(self, lblConversao, btnLimpar, btnConverter):
        '''Função que configura o botão de limpar resultado.'''
        lblConversao.destroy()
        btnLimpar.destroy()
        btnConverter['state'] = 'normal'

   
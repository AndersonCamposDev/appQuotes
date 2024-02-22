import requests

class Quotes:
    '''Classe responsável por fazer a chamada à API e obter todos os dados
    necessários para a criação da interface'''
    def __init__(self) -> None:
        self.url =  'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,CAD-BRL,AUD-BRL,JPY-BRL,GBP-BRL,SEK-BRL,BTC-BRL,MXN-BRL,CHF-BRL,RUB-BRL,ZAR-BRL,PLN-BRL,TRY-BRL,SGD-BRL'
        self.quotesList = []
        self.getQuotes()
        
    
    def getUrl(self):
        '''Faz a requisição à API e converte para o formato json'''
        self.r = requests.get(self.url)
        self.r_dict = self.r.json()

    def getQuotes(self):
        self.getUrl()
        '''Após a requisição à API, o dados são sintetizados e obtidos apenas aqueles estritamente necessários ao 
        funcionamento da aplicação.'''
        for key in self.r_dict:
            name = self.r_dict[key]['name'].split('/')
            name = name[0]
            if (key == 'BTCBRL'):
                quoteDict = {
                    'code':self.r_dict[key]['code'],
                    'codein': self.r_dict[key]['codein'],
                    'bid': float(self.r_dict[key]['bid']),
                    'name': name
                }
            elif (key == 'JPYBRL'):
                quoteDict = {
                    'code':self.r_dict[key]['code'],
                    'codein': self.r_dict[key]['codein'],
                    'bid': round(float(self.r_dict[key]['bid']), 3),
                    'name': name
                }
            else:
                quoteDict = {
                    'code':self.r_dict[key]['code'],
                    'codein': self.r_dict[key]['codein'],
                    'bid': round(float(self.r_dict[key]['bid']), 2),
                    'name': name
                }
            self.quotesList.append(quoteDict)




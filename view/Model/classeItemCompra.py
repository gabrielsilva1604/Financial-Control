import datetime

class ItemCompra:
    '''Esta classe representa um item de compra, ou seja, algum produto ou serviço que tenha
sido adquirido pelo usuário. Esta classe tem como atributos:nome,preço,data de compra,local de compra'''
    
    def __init__ (self,Nome,Preço,LocalCompra,DataCompra):
        self.__nome        =  Nome
        self.__Preço       =  Preço
        self.DataCompra    =  DataCompra
        self.LocalCompra   =  LocalCompra

        if type(self.__nome)!=str:
            raise TypeError('nome deve ser str')
        if type(self.__Preço)==str:
            raise TypeError('preço deve ser float')
        for letras in self.__nome:
            if letras in ['0','1','2','3','4','5','6','7','8','9']:
                raise TypeError('nome nao pode conter números')
        
    def __str__ (self):
        return(f'Nome: {self.__nome}\nPreço: {self.__Preço}\nData da compra: {self.DataCompra}\nLocal da compra: {self.LocalCompra}\n\n')

    #metodos get
    def nomeItem(self):
        return (self.__nome)

    def preço (self):
        return(self.__Preço)

    #metodos set
    def mudarPreço(self,novoPreço):
        if type(novoPreço)==str:
            raise TypeError('preço deve ser float')
        self.__Preço = novoPreço

    def mudarNome(self,novoNome):
        if type(novoNome)!=str:
            raise TypeError('nome deve ser str')
        self.__nome = novoNome
    
    def mudarData(self,novaData):
        self.DataCompra = novadata

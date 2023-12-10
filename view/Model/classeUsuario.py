class Usuario:
    '''esta classe moleda um usuario do sistema e tem como atributo: nome,senha,lista de itens comprados, lista de rendas'''
    def __init__(self,nome,senha,lista_de_itens,lista_de_renda):
        self.__nome=nome
        self.__senha=senha
        self.__lista_de_itens=lista_de_itens
        self.__lista_de_renda=lista_de_renda

        if type(self.__nome)!= str:
            raise TypeError('nome deve ser str')

        for letras in self.__nome:
            if letras in ['0','1','2','3','4','5','6','7','8','9']:
                raise TypeError('Usuario nao pode conter números')
#get/set     
    def nomeUsuario(self):
        return self.__nome

    def mudarNome(self,novoNome):
        if type(novoNome)!= str:
            raise TypeError('nome deve ser str')
        self.__nome=novoNome
        
    def senha(self):
        return self.__senha
    
    def mudarSenha(self,novasenha):
        self.__senha=novasenha

    def itens(self):
        return self.__lista_de_itens

    def novoItem(self,novoitem):
        self.__lista_de_itens.append(novoitem)
        
    def zeraritens(self):
        self.__lista_de_itens=[]

    def renda(self):
        return self.__lista_de_renda
    
    def novaRenda(self,novarenda):
        self.__lista_de_renda.append(novarenda)
        
    def zerarRenda(self):
        self.__lista_de_renda=[]
#tostring
    def __str__(self):
        return f'nome:{self.__nome}\nsenha:{self.__senha}\nlista de itens:{self.__lista_de_itens}\nlista de renda:{self.__lista_de_renda}'
        

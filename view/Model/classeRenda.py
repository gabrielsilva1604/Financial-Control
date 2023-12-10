class Renda:
    '''Esta classe representa uma fonte de renda, ou seja, algum meio pelo qual o usuário ganha
dinheiro. Esta classe tem como atributos:nome,valor,data de recebimento,fonte'''

    def __init__(self,nome,valor,data_de_recebimento,fonte):
        self.__nome=nome
        self.__valor=valor
        self.data_de_recebimento=data_de_recebimento   
        self.fonte=fonte

        if type(self.__nome)!= str:
            raise TypeError('nome deve ser str')

        if type(self.__valor)==str:
            raise TypeError('valor deve ser float')

        for letras in self.__nome:
            if letras in ['0','1','2','3','4','5','6','7','8','9']:
                raise TypeError('nome nao pode conter números')

#get/set     


    def __str__(self):
        return f'nome:{self.__nome}\nvalor:{self.__valor}\ndata de recebimento:{self.data_de_recebimento}\nfonte:{self.fonte}\n\n'
    
    # metodos get/set
    def nome(self):
        return self.__nome
    def mudarNome(self,novoNome):
         if type(novoNome)!= str:
             
            raise TypeError('nome deve ser str')
         self.__nome=novoNome

    def valor(self):
        return self.__valor
    def mudarvalor(self,novoValor):
         if type(novoValor)==str:
            raise TypeError('valor deve ser float')
         self.__valor=novoValor

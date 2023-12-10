from tkinter import*
from tkinter import messagebox
from Model.classeItemCompra import *
from Model.classeRenda import *
from Model.classeUsuario import*
import telaCadastroi
import pickle
import os

class Controle(Tk):
    def __init__(self,nome):
        super(Controle,self).__init__()
        
        #self.JanelaCadastroi=JanelaCadastroi
        self.n=nome
        
        self.title('Controle de Finanças')
        self.geometry('400x270')

        self.frame1=Frame(self)
        self.frame1.pack()
        
        self.lblx=Label(self.frame1,text='Total: R$ 0.00',font=('Arial 12 bold'))
        self.lblx.pack()

        #scroll
        self.frame2=Frame(self)
        self.frame2.pack()

        self.scrollbarY=Scrollbar(self.frame2,orient=VERTICAL)
        self.scrollbarY.pack(side=RIGHT,fill=Y)

        self.scrollbarX = Scrollbar(self.frame2, orient=HORIZONTAL)
        self.scrollbarX.pack(side=BOTTOM, fill=X)

        
        
        #listbox
        self.lb=Listbox(self.frame2,yscrollcommand=self.scrollbarY.set,xscrollcommand=self.scrollbarX.set,width=50,height=10,font=('Arial 10 bold '),bd=10)
        self.lb.pack()
        
        # Configura o scrollbar como scroll da Listbox
        self.scrollbarY.config(command=self.lb.yview)
        self.scrollbarX.config(command=self.lb.xview)
        try:
            arquivoAberto=open('cadastro.pkl','rb')
            lista1=pickle.load(arquivoAberto)
        except IOError as err:
            messagebox.showerror('erro',f'{err}')
        finally:
            arquivoAberto.close()
            
        
        
        nomes=[]
        for objetos in lista1:
            nomes.append(objetos.nomeUsuario())
      
        self.x=nomes.index(self.n)
        itens=lista1[self.x].itens()

        self.gastos=0
        if len(itens)>0:
            for i in itens:
                self.gastos+=i.preço()
                self.lb.insert(END,f'{i.DataCompra} - {i.nomeItem()} - {i.LocalCompra} - {i.preço()}')
          
        else:
            pass
        

        renda=lista1[self.x].renda()
        self.ganhos=0
        if len(renda)>0:
            for R in renda:
                self.ganhos+=R.valor()
                self.lb.insert(END,f'{R.data_de_recebimento} - {R.nome()} - {R.fonte} - {R.valor()}')
        else:
            pass
        
        self.total=self.ganhos-self.gastos
        if self.total>0:
            self.lblx.config(text=f'Total: R$ {self.total}',fg='blue')
        elif self.total<0:
            self.lblx.config(text=f'Total: R$ {self.total}',fg='red')
        else:
            self.lblx.config(text=f'Total: R$ {self.total}')
            
        
        #botoes
        self.frame3=Frame(self)
        self.frame3.pack()

        self.botao1=Button(self.frame3,text='Cadastrar Item')
        self.botao1.pack(side=LEFT)
        self.botao1.bind('<ButtonRelease-1>',self.cadastrarItem)

        self.botao2=Button(self.frame3,text='Limpar')
        self.botao2.pack(side=LEFT)
        self.botao2.bind('<ButtonRelease-1>',self.limpar)

        self.botao3=Button(self.frame3,text='Gerar Relatório')
        self.botao3.pack()
        self.botao3.bind('<ButtonRelease-1>',self.gerar)



    #funçao do gerar relatorio

    def gerar(self,event):
        try:
            arquivoAberto=open('cadastro.pkl','rb')
            lista1=pickle.load(arquivoAberto)
        except IOError as err:
            messagebox.showerror('erro',f'{err}') 
        finally:
            arquivoAberto.close()
        try:
            arquivo=open(f'relatório_{self.n}.txt','w')
            itens=lista1[self.x].itens()
            listacomprintdositens=[]
            for i in itens:
                listacomprintdositens.append(i.__str__())

            renda=lista1[self.x].renda()
            listacomprintdosrenda=[]
            for R in renda:
                listacomprintdosrenda.append(R.__str__())
                
            arquivo.write(f'saldo:R$ {self.total}\n\n')   
            arquivo.write('Itens de compra:\n\n')   
            arquivo.writelines(listacomprintdositens)
            arquivo.write('Itens de Renda:\n\n')
            arquivo.writelines(listacomprintdosrenda)
            messagebox.showinfo('aviso',f'relatório foi salvo com sucesso dentro da pasta view\ncom o nome: relatório_{self.n}')
        except IOError as err:
            messagebox.showerror('erro',f'{err}')
        finally:
            arquivo.close()
    #funçao do limpar
    def limpar(self,event):
        self.lb.delete(0,END)
        
        try:
            arquivoAberto=open('cadastro.pkl','rb')
            lista1=pickle.load(arquivoAberto)
        except IOError as err:
            messagebox.showerror('erro',f'{err}')
        finally:
            arquivoAberto.close()

        lista1[self.x].zerarRenda()
        lista1[self.x].zeraritens()
        
        try:
            arquivo=open('cadastro.pkl','wb')
            pickle.dump(lista1,arquivo)
        except IOError as err:
            messagebox.showerror('erro',f'{err}')
        finally:
            arquivo.close()

        self.gastos=0
        self.ganhos=0
        self.total=self.ganhos-self.gastos
   
        self.lblx.config(text=f'Total: R$ {self.total}',fg='black')

        

     #funçao do botao cadastrar item   
    def cadastrarItem(self,event):
        self.cadastroitem=telaCadastroi.CadastroItem(self.n)
        self.cadastroitem.deiconify()
        self.destroy()
        


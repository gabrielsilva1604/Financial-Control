from tkinter import*
from tkinter import messagebox
from Model.classeItemCompra import *
from Model.classeRenda import *
from Model.classeUsuario import*
import telaControleF 
import datetime
import pickle
import os

class CadastroItem(Tk):
    def __init__(self,nome):
        Tk.__init__(self)
        
        self.n=nome
        
        self.title('Cadastro de Item')
        self.geometry('200x200')
        self.label1=Label(self,text='Cadastro de item',font=('Arial 10 bold'))
        self.label1.pack()

        #nome do item
        self.label2=Label(self,text='Nome de item:')
        self.label2.pack()
        self.label2.place(y=20,x=10)

        self.E1=Entry(self)
        self.E1.pack()
        self.E1.place(y=20,x=95)

        #preço
        self.label3=Label(self,text='Preço:')
        self.label3.pack()
        self.label3.place(y=45,x=55)

        self.E2=Entry(self)
        self.E2.pack()
        self.E2.place(y=45,x=95)

        #local de compra

        self.label4=Label(self,text='Local de compra:')
        self.label4.pack()
        self.label4.place(y=70,)

        self.E3=Entry(self)
        self.E3.pack()
        self.E3.place(y=70,x=95)

        #data
        self.label5=Label(self,text='Data:')
        self.label5.pack()
        self.label5.place(y=95,x=60)

        
        
        self.agora=datetime.datetime.now()
        self.agora_string=self.agora.strftime("%d/%m/%Y %H:%M")

        self.E4=Entry(self)
        self.E4.insert(END,f'{self.agora_string}')
        self.E4.pack()
        self.E4.place(y=95,x=95)

        

        #botao salvar
        self.botao1=Button(self,text='Salvar')
        self.botao1.pack()
        self.botao1.place(y=120,x=85)
        self.botao1.bind('<ButtonRelease-1>',self.salvar1)
        
        #Radiobuttton
    
        
        self.selecionado = StringVar()
               
        self.rb1=Radiobutton(self,text='Compra',variable=self.selecionado,value=1)
        self.rb1.pack()
        self.rb1.place(y=120)
        self.rb1.bind('<ButtonRelease-1>',self.obter1)
       

        self.rb2=Radiobutton(self,text='Renda',variable=self.selecionado,value=2)
        self.rb2.pack()
        self.rb2.place(y=140)
        self.rb2.bind('<ButtonRelease-1>',self.obter2)
        
       
    def obter1(self,event):
        self.label4.config(text='Local de compra:')
        self.selecionado.set(1)
        
        
        
    def obter2(self,event):
        self.label4.config(text='                   fonte:')
        self.selecionado.set(2)
        
    

      
    #salvar cadastro de item    
    def salvar1(self,event):      
        if self.selecionado.get()=='1':
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
            x=nomes.index(self.n)
            
            try:
                datetime.datetime.strptime(self.E4.get(),"%d/%m/%Y %H:%M")
                e='ok'
            except:
                e='erro'
            if e =='erro':
                messagebox.showerror('erro','Data nao está no mesmo formato dia/mês/ano hora:minuto')
            else:
                try:     
                    c=ItemCompra(self.E1.get(),float(self.E2.get()),self.E3.get(),self.E4.get())
                    lista1[x].novoItem(c)

                    try:
                        arquivo=open('cadastro.pkl','wb')
                        pickle.dump(lista1,arquivo)
                    except IOError as err:
                        messagebox.showerror('erro',f'{err}')
                    finally:
                        arquivo.close()
                    
                    self.controle=telaControleF.Controle(self.n)
                    self.controle.deiconify()
                    self.destroy()
                except Exception as error:
                    messagebox.showerror('Erro',f'{error}') 
                    
            
            
            
        elif self.selecionado.get()=='2':
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
            x=nomes.index(self.n)
            
            try:
                datetime.datetime.strptime(self.E4.get(),"%d/%m/%Y %H:%M")
                e='ok'
            except:
                e='erro'
            if e =='erro':
                messagebox.showerror('erro','Data nao está no mesmo formato dia/mês/ano hora:minuto')
            else:
                try:
                    R=Renda(self.E1.get(),float(self.E2.get()),self.E4.get(),self.E3.get())
                    lista1[x].novaRenda(R)
                    try:
                        arquivo=open('cadastro.pkl','wb')
                        pickle.dump(lista1,arquivo)
                    except IOError as err:
                        messagebox.showerror('erro',f'{err}')
                    finally:
                        arquivo.close()

                    
                    self.controle=telaControleF.Controle(self.n)
                    self.controle.deiconify()
                    self.destroy()
                except Exception as error:
                    messagebox.showerror('Erro',f'{error}')
                 
        else:
            messagebox.showerror('erro','escolha se é do tipo compra ou renda')
            

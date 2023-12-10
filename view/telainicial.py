from tkinter import*
from tkinter import messagebox
from Model.classeItemCompra import *
from Model.classeRenda import *
from Model.classeUsuario import*
import telaCadastroP
import telaControleF
import pickle
import os


class Inicial(Tk):
    def __init__(self):
        super(Inicial,self).__init__()
        self.title('Controle de Finanças')
        self.fr1=Frame(self)
        self.fr1.pack()
        #label controle de finanças
        self.lbl1=Label(self.fr1,text='Controle de Finanças',font=('Arial 11 bold '))
        self.lbl1.pack()
        #usuario
        self.lbl2=Label(self.fr1,text='Usuário:',font=9)
        self.lbl2.pack(side=LEFT)

        self.entry1=Entry(self.fr1,bd=5)
        self.entry1.pack(side=LEFT)
        #senha
        self.fr2=Frame(self)
        self.fr2.pack()

        self.lbl3=Label(self.fr2,text='Senha:',font=9)
        self.lbl3.pack(side=LEFT)

        self.entry2=Entry(self.fr2,bd=5,show='*')
        self.entry2.pack(side=LEFT)

        self.fr3=Frame(self)
        self.fr3.pack()
        #botao cadastrar
        self.b1=Button(self.fr3,text='Cadastrar',bg='#6495ED')
        self.b1.bind('<Button-1>',self.cadastro1)
        self.b1.pack(side=LEFT)
        
        #botao entrar
        self.b2=Button(self.fr3,text='Entrar',bg='#228B22')
        self.b2.bind('<ButtonRelease-1>',self.entrar)
        self.b2.pack(side=LEFT)
        
       
       


    #metodo do cadastro
    def cadastro1(self,event):
        
        self.cadastro=telaCadastroP.Cadastro(self)
        self.cadastro.deiconify()
        self.withdraw()
        


#metodo entrar          
    def entrar(self,event):
       
        if f'{self.entry1.get()}'=='' or f'{self.entry2.get()}'=='':
            messagebox.showerror('Erro','Campo da senha ou usuário vazios')
        
        elif os.path.exists('cadastro.pkl'):  
            
            try:
                try:
                    arquivoAberto=open('cadastro.pkl','rb')
                    lista1=pickle.load(arquivoAberto)
                except IOError as err:
                    messagebox.showerror('erro',f'{err}')
                finally:
                    arquivoAberto.close()
            
            
                w=['']
                for objetos in lista1:
                    if self.entry1.get()== objetos.nomeUsuario() and self.entry2.get()== objetos.senha():
                        w=[]
                        w.append(objetos)
                        
                if self.entry1.get() == w[0].nomeUsuario() and self.entry2.get()==w[0].senha():
                    n=self.entry1.get()
                    
                    self.controle=telaControleF.Controle(n)
                    self.controle.deiconify()
                    self.withdraw()
                        
                else:
                    messagebox.showerror('Erro','usuário ou senha não cadastrados')
            except IOError as e:
                messagebox.showerror('Erro',f'{e}')
                    
                
        else:
            messagebox.showerror('Erro','nao ha cadastros ainda')
            

        

if __name__=='__main__':
    inicial=Inicial()
    inicial.geometry('350x200')
    inicial.mainloop()



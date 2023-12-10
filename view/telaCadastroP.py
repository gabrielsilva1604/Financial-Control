from tkinter import*
from tkinter import messagebox
from Model.classeItemCompra import *
from Model.classeRenda import *
from Model.classeUsuario import*
import pickle
import os

class Cadastro(Tk):
    def __init__(self,JanelaInicial):
        
        super(Cadastro,self).__init__()
        
        self.JanelaInicial=JanelaInicial
        
        self.title('Cadastro de Usuário')
        self.geometry('210x130')
        #label de cadastro
        
        self.lbl1=Label(self,text='Cadastro de Usuário',font=('Arial 11 bold')).place(x=30)
    
        #usuario
        
        
        self.lbl2=Label(self,text='Usuário:').place(x=45,y=20)
       

        self.entry3=Entry(self)
        self.entry3.pack()
        self.entry3.place(x=95,y=20)

        

        #senha
        self.lbl3=Label(self,text='Senha:').place(x=51,y=40)
        

        self.entry4=Entry(self,show='*')
        self.entry4.pack()
        self.entry4.place(x=95,y=40)
        
        #confirme senha
        self.lbl4=Label(self,text='Confirme Senha:').place(x=0,y=60)
        

        self.entry5=Entry(self,show='*')
        self.entry5.pack()
        self.entry5.place(x=95,y=60)

        #botao salvar
        self.b3=Button(self,text='Salvar')
        self.b3.pack()
        self.b3.place(x=90,y=80)
        self.b3.bind('<ButtonRelease-1>',self.salvar)
#metodo salvar
        
    def salvar(self,event):
        if self.entry4.get()!=self.entry5.get():
            messagebox.showerror('senhas diferentes','senhas diferentes')
            
        elif f'{self.entry3.get()}'=='' or f'{self.entry4.get()}'=='':
            messagebox.showerror('Erro','Campo da senha ou usuário vazios')
                
        else:
            try:
                u=Usuario(self.entry3.get(),self.entry4.get(),[],[])
                lista=[]
                lista.append(u)
                
            # ve se p arquivo existe caso exista desserializa a lista que ja estava salva
            #e adiciona o novo objeto e depois serializa a lista com o novo objeto

                if os.path.exists('cadastro.pkl'):
                    try:
                        arquivoAberto=open('cadastro.pkl','rb')
                        lista1=pickle.load(arquivoAberto)
                    except IOError as err:
                        messagebox.showerror('erro',f'{err}')
                    finally:
                        arquivoAberto.close()
                        
                    
                    
                    # ve se o usuario ja foi cadastrado
                    nomes=[]
                    for objetos in lista1:
                        nomes.append(objetos.nomeUsuario())
                        
                    if u.nomeUsuario() in nomes:
                        messagebox.showerror('Erro','nome de usuário já cadastrado')
                   

                    else:
                    
                        lista1.append(u)
                        try:
                            arquivo=open('cadastro.pkl','wb')
                            pickle.dump(lista1,arquivo)
                        except IOError as err:
                            messagebox.showerror('erro',f'{err}')
                        finally:
                            arquivo.close()
                            
                    
                        self.JanelaInicial.deiconify()
                        self.withdraw()
                
                            
                            
                            
                            
                            
                            
                    
                    
                #caso o arquivo nao exista cria o arquivo e serializa a lista com o primeiro arquivo   
                else:
                    try:
                        arquivo=open('cadastro.pkl','wb')
                        pickle.dump(lista,arquivo)
                    except IOError as err:
                        messagebox.showerror('erro',f'{err}')
                    finally:
                        arquivo.close()

                    self.JanelaInicial.deiconify()
                    self.withdraw()
                

                
            except Exception as error:
                messagebox.showerror('Erro',f'{error}')
                
           
                
                
                
        
            
     



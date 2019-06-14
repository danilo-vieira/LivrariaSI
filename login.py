from tkinter import *
import tkinter as tk
from tkinter import messagebox
import shelve
import os

path = os.path.dirname(os.path.abspath(__file__))

class Gerenciador(tk.Tk):

	def __init__(self,*args,**wargs):
		tk.Tk.__init__(self,*args,**wargs)
		tk.Tk.iconbitmap(self,default = path + '\images\icone.ico' )
		tk.Tk.wm_title(self,"Login")
		#tk.Tk.background='black'
		self.auto = self
		self.container = Frame(self)
		self.container.pack(side="top",fill="both",expand=True)
		self.container.grid_rowconfigure(0,weight=1)
		self.container.grid_columnconfigure(0,weight=1)
		self.TELAS = [LoginInicial,FuncionarioOp]
		self.frames = {}
		for tela in (self.TELAS):
			frame = tela(self.container,self)
			self.frames[tela] = frame
			frame.grid(row=0,column=0,stick="nsew")
		self.trocar_janela_por(LoginInicial)
		
	def trocar_janela_por(self,count):
		self.atualizar(count)
		frame = self.frames[count]
		frame.tkraise()

	def atualizar(self,count):
		self.TELAS.remove(count)
		self.TELAS.append(count)
		del self.frames[count]
		frame = count(self.container,self)
		self.frames[count] = frame
		frame.grid(row=0,column=0,stick="nsew")

class LoginInicial(Frame):
        def __init__(self,parent,controler):
                Frame.__init__(self,parent)
                self.frame_atual = Frame(self, pady=130)
                self.frame_atual.pack()
                self.photo = PhotoImage(file = path + '\images\\telaLogin.png')
                self.foto = Label(self.frame_atual, image = self.photo ,padx=300)
                self.foto.pack()
                self.userText = Label(self.frame_atual, text='Usuário')
                self.userText.pack()
                self.userForm = Entry(self.frame_atual, width = 25)
                self.userForm.pack()
                self.passText = Label(self.frame_atual, text='Senha')
                self.passText.pack()
                self.passForm = Entry(self.frame_atual, show='*', width = 25)
                self.passForm.pack()
                self.frame_botoes = Frame(self,pady=10)
                self.frame_botoes.pack()
                self.bt = Button(self.frame_botoes, text='Entrar', command = lambda:self.Verifica(controler), width = 25)
                #self.bt.pack()
                self.bt.grid(row=0,column=0)
                self.sair = Button(self.frame_botoes, text='Sair', command = self.quit, width = 25)
                #self.sair.pack()
                self.sair.grid(row=0,column=10)
        def Verifica(self,controler):
                db = shelve.open(path + '\\arquivosdb\\login\\login.db')
                if self.userForm.get()=='':
                    messagebox.showwarning('Aviso', 'Preencha o Usuário')
                elif(self.userForm.get() in db['User'] and self.passForm.get() in db['Pass']):
                    controler.trocar_janela_por(FuncionarioOp)
                elif(self.userForm.get() not in db['User']):
                    messagebox.showwarning("Aviso", "Usuário invalido!")
                else:
                    messagebox.showwarning("Aviso", "Senha invalida!")

class FuncionarioOp(Frame):
        def __init__(self,parent,controler):
                Frame.__init__(self,parent)
                self.i = Frame(self, pady=70)
                self.i.pack()
                self.addLivro = Button(self.i, text = "Adicionar Livro", width = 13, command = self.Alerta)
                self.addLivro.pack()
                self.removeLivro = Button(self.i, text = "Remover Livro", width = 13, command = self.Alerta)
                self.removeLivro.pack()
                self.validaCompra = Button(self.i, text = "Validar Compra", width = 13, command = self.Alerta)
                self.validaCompra.pack()
                self.subframe = Frame(self.i)
                self.subframe.pack()
                self.voltar = Button(self.subframe, text = "Fazer Logout", width = 13, command = lambda:controler.trocar_janela_por(LoginInicial))
                self.voltar.pack(pady = 60)
        
        def Alerta(self):
            messagebox.showwarning("Aviso", "Área não implementada!")

def main():
	app = Gerenciador()
	app.mainloop()
if __name__ == '__main__':
	main()




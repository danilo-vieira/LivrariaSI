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
		tk.Tk.wm_title(self,"Cadastro de Funcionários")
		tk.Tk.background='black'
		self.auto = self
		self.container = Frame(self)
		self.container.pack(side="top",fill="both",expand=True)
		self.container.grid_rowconfigure(0,weight=1)
		self.container.grid_columnconfigure(0,weight=1)
		self.TELAS = [TelaCadastro]
		self.frames = {}
		for tela in (self.TELAS):
			frame = tela(self.container,self)
			self.frames[tela] = frame
			frame.grid(row=0,column=0,stick="nsew")
		self.trocar_janela_por(TelaCadastro)
		
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

class TelaCadastro(Frame):
        def __init__(self,parent,controler):
                Frame.__init__(self,parent)
                self.frame_atual = Frame(self, pady=60)
                self.frame_atual.pack()
                self.photo = PhotoImage(file = path +'\images\\telaAdmin.png')
                self.foto = Label(self.frame_atual, image = self.photo ,padx=300)
                self.foto.pack()
                self.userText = Label(self.frame_atual, text='Nome do funcionário')
                self.userText.pack()
                self.userForm = Entry(self.frame_atual, width = 25)
                self.userForm.pack()
                self.passText = Label(self.frame_atual, text='Senha do funcionário')
                self.passText.pack()
                self.passForm = Entry(self.frame_atual, show='*', width = 25)
                self.passForm.pack()
                self.confText = Label(self.frame_atual, text='Confirme a senha')
                self.confText.pack()
                self.confForm = Entry(self.frame_atual, show='*', width = 25)
                self.confForm.pack()
                self.frame_botoes = Frame(self, pady = 20)
                self.frame_botoes.pack()
                self.bt = Button(self.frame_botoes, relief=RIDGE, text='Cadastrar', command = lambda:self.Cadastra(controler), width = 25)
                self.bt.grid(row=0,column=0)

        def Cadastra(self,controler):
                self.db = shelve.open(path + '\\arquivosdb\\login\\login.dat')
                if self.userForm.get()=='':
                    messagebox.showwarning('Aviso', 'Preencha o Usuario')
                elif self.passForm.get()=='':
                    messagebox.showwarning('Aviso', 'Preencha a Senha')
                elif(self.passForm.get() != self.confForm.get()):
                    messagebox.showerror("Aviso", "As senhas não coincidem")
                else:
                    self.user = self.userForm.get()
                    self.db[self.user] = self.passForm.get()
                    self.db.close()
                    messagebox.showinfo('Concluído', 'O funcionário ' + self.userForm.get() + ' foi cadastrado')

def main():
	app = Gerenciador()
	app.mainloop()
if __name__ == '__main__':
	main()
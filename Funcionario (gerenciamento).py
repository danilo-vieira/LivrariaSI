from tkinter import *
import tkinter as tk
from tkinter import messagebox
import shelve
import os
path = os.path.dirname(os.path.abspath(__file__))

class Gerenciador(tk.Tk):

	def __init__(self,*args,**wargs):
		tk.Tk.__init__(self,*args,**wargs)
		tk.Tk.iconbitmap(self,default = path + '\\images\icone.ico' )
		tk.Tk.wm_title(self,"Login")
		self.auto = self
		self.container = Frame(self)
		self.container.pack(side="top",fill="both",expand=True)
		self.container.grid_rowconfigure(0,weight=1)
		self.container.grid_columnconfigure(0,weight=1)
		self.TELAS = [LoginInicial, FuncionarioOp, AdcLivro, RmvLivro, ValidaCompra]
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
        self.photo = PhotoImage(file = path + '\\images\\telaLogin.png')
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
        self.bt.grid(row=0,column=0)
        self.bt.bind("<Return>", lambda e: self.Verifica(controler) if e.char == '\r' else None)
        self.sair = Button(self.frame_botoes, text='Sair', command = self.quit, width = 25)
        self.sair.grid(row=0,column=10)
    def Verifica(self,controler):
            self.db = shelve.open(path + '\\arquivosdb\\login\\login.dat')
            if self.userForm.get()=='':
                messagebox.showwarning('Aviso', 'Preencha o Usuário!')
            elif self.passForm.get()=='':
                messagebox.showwarning('Aviso', 'Preencha a Senha!')
            elif(self.userForm.get() in self.db):
                if(self.passForm.get() == self.db[self.userForm.get()]):
                    self.db.close()
                    controler.trocar_janela_por(FuncionarioOp)
                else:
                    messagebox.showerror("Aviso", "Senha invalida!")
                    self.passForm.delete(first = 0, last = END)
            elif(self.userForm.get() not in self.db):
                messagebox.showerror("Aviso", "Usuário invalido!")
                self.userForm.delete(first = 0, last = END)
                self.passForm.delete(first = 0, last = END)
                self.userForm.focus()

class FuncionarioOp(Frame):
    def __init__(self,parent,controler):
        Frame.__init__(self,parent)
        self.i = Frame(self, pady=70)
        self.i.pack()
        self.labelCentral = Label(self.i, text = "Gerenciamento", font = "Arial 32 bold ")
        self.labelCentral.pack(pady = 40)
        self.addLivro = Button(self.i, text = "Adicionar Livro", width = 13, command = lambda:controler.trocar_janela_por(AdcLivro))
        self.addLivro.pack()
        self.removeLivro = Button(self.i, text = "Remover Livro", width = 13, command = lambda:controler.trocar_janela_por(RmvLivro))
        self.removeLivro.pack()
        self.validaCompra = Button(self.i, text = "Validar Compra", width = 13, command = lambda:controler.trocar_janela_por(ValidaCompra))
        self.validaCompra.pack()
        self.subframe = Frame(self.i)
        self.subframe.pack()
        self.voltar = Button(self.subframe, text = "Fazer Logout", width = 13, command = lambda:controler.trocar_janela_por(LoginInicial))
        self.voltar.pack(pady = 60)

class AdcLivro(Frame):
    def __init__(self,parent,controler):
        Frame.__init__(self,parent)
        self.frame_atual = Frame(self, pady=70)
        self.frame_atual.pack()

        self.labelCentral = Label(self.frame_atual, text = "Adicionar Livro", font = "Arial 32 bold ")
        self.labelCentral.pack(pady = 40)

        self.lblNomeLivro = Label(self.frame_atual, text = "Título do livro")
        self.lblNomeLivro.pack()
        self.entryTitle = Entry(self.frame_atual, width = 25)
        self.entryTitle.pack()

        self.lblQtd = Label(self.frame_atual, text = "Quantidade")
        self.lblQtd.pack()
        self.entryQtd = Entry(self.frame_atual, width = 25)
        self.entryQtd.pack()

        self.lblGen = Label(self.frame_atual, text = "Gênero")
        self.lblGen.pack()
        self.entryGen = Entry(self.frame_atual, width = 25)
        self.entryGen.pack()

        self.lblAuthor = Label(self.frame_atual, text = "Autor")
        self.lblAuthor.pack()
        self.entryAuthor = Entry(self.frame_atual, width = 25)
        self.entryAuthor.pack()

        self.lblPrice = Label(self.frame_atual, text = "Preço")
        self.lblPrice.pack()
        self.entryPrice = Entry(self.frame_atual, width = 25)
        self.entryPrice.pack()

        self.frame_botoes = Frame(self.frame_atual, pady = 30)
        self.frame_botoes.pack()
        self.adc = Button(self.frame_botoes, text='Adicionar', width = 13, command =  lambda: self.Adiciona(controler))
        self.adc.grid(row=0,column=0)
        self.btnVoltar = Button(self.frame_botoes, text='Voltar', width = 13, command = lambda:controler.trocar_janela_por(FuncionarioOp))
        self.btnVoltar.grid(row=0,column=10)

    def Adiciona(self, controler):
        if (self.entryTitle.get()=='' or
        self.entryQtd.get()=='' or
        self.entryGen.get()=='' or
        self.entryAuthor.get()=='' or
        self.entryPrice.get()==''):
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
        else:
            self.livros = shelve.open(path + '\\arquivosdb\\livros\\livros.dat')
            self.livros[self.entryTitle.get()] = {
            'qtd': int(self.entryQtd.get()),
            'gen': self.entryGen.get(),
            'author': self.entryAuthor.get(),
            'price': float(self.entryPrice.get())
            }
            self.livros.close()
            messagebox.showinfo("Concluido", "Livro adicionado!")
            self.entryTitle.delete(first = 0, last = END)
            self.entryQtd.delete(first = 0, last = END)
            self.entryGen.delete(first = 0, last = END)
            self.entryAuthor.delete(first = 0, last = END)
            self.entryPrice.delete(first = 0, last = END)
            self.entryTitle.focus()

class RmvLivro(Frame):
    def __init__(self,parent,controler):
        Frame.__init__(self,parent)
        self.frame_atual = Frame(self, pady=70)
        self.frame_atual.pack()
        self.labelCentral = Label(self.frame_atual, text = "Remover Livro do Estoque", font = "Arial 32 bold ")
        self.labelCentral.pack()

        self.labelSec = Label(self.frame_atual, text = "Atenção! Essa opção irá remover todas as unidades em estoque!", font = "Arial")
        self.labelSec.pack(pady = 40)

        self.lblNomeLivro = Label(self.frame_atual, text = "Título do livro")
        self.lblNomeLivro.pack()
        self.entryTitle = Entry(self.frame_atual, width = 25)
        self.entryTitle.pack()

        self.frame_botoes = Frame(self.frame_atual, pady = 30)
        self.frame_botoes.pack()
        self.adc = Button(self.frame_botoes, text='Remover', width = 13, fg = 'red', command =  lambda: self.Remove(controler))
        self.adc.grid(row=0,column=0)
        self.btnVoltar = Button(self.frame_botoes, text='Voltar', width = 13, command = lambda:controler.trocar_janela_por(FuncionarioOp))
        self.btnVoltar.grid(row=0,column=10)

    def Remove(self, controler):
        self.livros = shelve.open(path + '\\arquivosdb\\livros\\livros.dat')
        if(self.entryTitle.get() in self.livros):
            del self.livros[self.entryTitle.get()]
            self.livros.close()
            messagebox.showinfo("Concluido", "Livro removido!")
            self.entryTitle.delete(first = 0, last = END)
        else:
            messagebox.showerror("Ops", "Livro não encontrado!\nTalvez já tenha sido removido ;)")

class ValidaCompra(Frame):
    def __init__(self,parent,controler):
        Frame.__init__(self,parent)
        self.frame_atual = Frame(self, pady=70)
        self.frame_atual.pack()
        self.labelCentral = Label(self.frame_atual, text = "Validar compras", font = "Arial 32 bold ")
        self.labelCentral.pack()
        self.labelCentral = Label(self.frame_atual, text = "Digite o CPF", font = "Arial")
        self.labelCentral.pack()
        self.cpf = Entry(self.frame_atual, width = 25)
        self.cpf.pack()
        self.frame_botoes = Frame(self,pady=10)
        self.frame_botoes.pack()
        self.bt = Button(self.frame_botoes, text='Aprovar', command = lambda:self.Verifica(controler), width = 25)
        self.bt.grid(row=0,column=0)

    def Verifica(self, controler):
        self.pedidos = shelve.open(path + '\\arquivosdb\\pedidos\\pedidos.dat')
        self.livros = shelve.open(path + '\\arquivosdb\\livros\\livros.dat')
        if(self.cpf.get() not in self.pedidos):
            messagebox.showerror("Erro", "Não houve pedido encontrado")
        else:
            self.title = self.pedidos[self.cpf.get()]
            self.qtd = self.livros[self.title]['qtd']
            self.qtd -= 1
            self.livros[self.title]['qtd'] = self.qtd
            messagebox.showinfo("Concluído", "Pedido confirmado!")
            self.cpf.delete(first = 0, last = END)
            if(self.livros[self.title]['qtd'] == 0):
                del self.livros[self.title]
            self.pedidos.close()
            self.livros.close()

        

def main():
	app = Gerenciador()
	app.mainloop()
if __name__ == '__main__':
	main()




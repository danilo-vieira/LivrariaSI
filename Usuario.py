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
		self.TELAS = [TelaInicial, Resultado]
		self.frames = {}
		for tela in (self.TELAS):
			frame = tela(self.container,self)
			self.frames[tela] = frame
			frame.grid(row=0,column=0,stick="nsew")
		self.trocar_janela_por(TelaInicial)
		
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

class TelaInicial(Frame):
    def __init__(self,parent,controler):
        Frame.__init__(self,parent)
        self.frame_atual = Frame(self, pady=130)
        self.frame_atual.pack()
        self.photo = PhotoImage(file = path + '\\images\\telaLogin.png')
        self.foto = Label(self.frame_atual, image = self.photo ,padx=300)
        self.foto.pack()
        self.userText = Label(self.frame_atual, text='Buscar por Título', font = "bold")
        self.userText.pack(pady = 40)
        self.titleForm = Entry(self.frame_atual, width = 25)
        self.titleForm.pack()
        self.frame_botoes = Frame(self,pady=10)
        self.frame_botoes.pack()
        self.bt = Button(self.frame_botoes, text='Buscar', command = lambda:self.Busca(controler), width = 25)
        self.bt.grid(row=0,column=0)
        self.bt.bind("<Return>", lambda e: self.Busca(controler) if e.char == '\r' else None)
        self.sair = Button(self.frame_botoes, text='Sair', command = self.quit, width = 25)
        self.sair.grid(row=0,column=10)
    def Busca(self,controler):
            self.livros = shelve.open(path + '\\arquivosdb\\livros\\livros.dat')
            if self.titleForm.get()=='':
                messagebox.showwarning('Aviso', 'Por favor, preencha o campo de busca!')
            elif(self.titleForm.get() not in self.livros):
                    messagebox.showerror("Erro", "O livro buscado não foi encontrado em nosso estoque :(\n")
                    self.titleForm.delete(first = 0, last = END)
                    self.titleForm.focus()
            else:
                self.busca = shelve.open(path + '\\arquivosdb\\busca\\busca.dat')
                self.busca[' '] = self.titleForm.get()
                self.busca.close()
                controler.trocar_janela_por(Resultado)
            self.livros.close()
class Resultado(Frame):
    pass
    def __init__(self,parent,controler):
        Frame.__init__(self,parent)
        self.frame_atual = Frame(self, pady=70)
        self.frame_atual.pack()
        self.result = Label(self.frame_atual, text = "Sua busca retornou um resultado!")
        self.result.pack(pady = 40)
        self.livro = shelve.open(path + '\\arquivosdb\\livros\\livros.dat')
        self.busca = shelve.open(path + '\\arquivosdb\\busca\\busca.dat')
        
        self.title = self.busca[' ']
        self.gen = self.livro[self.title]['gen']

        self.result = Label(self.frame_atual, text = "Título: " + self.title)
        self.result.pack()

        self.result = Label(self.frame_atual, text = "Gênero: " + self.gen)
        self.result.pack()
        
        self.result = Label(self.frame_atual, text = "Por favor, preencha o campo com seu CPF\ne clique em 'Comprar'", font = 'Arial 12 bold')
        self.result.pack()
        self.frame_botoes = Frame(self,pady=10)
        self.frame_botoes.pack()
        self.bt = Button(self.frame_botoes, text='COMPRAR', command = lambda:self.Busca(controler), width = 25)
        self.bt.grid(row=0,column=0)
        self.bt.bind("<Return>", lambda e: self.Busca(controler) if e.char == '\r' else None)
        self.sair = Button(self.frame_botoes, text='Sair', command = self.quit, width = 25)
        self.sair.grid(row=0,column=10)
def main():
	app = Gerenciador()
	app.mainloop()
if __name__ == '__main__':
	main()
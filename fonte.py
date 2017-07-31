from tkinter import *

class TelaPrincipal:
	def __init__(self, janela):
		self.janela = janela 
		self.janela.resizable(0,0)
		self.fundo = "black"
		self.janela["background"] = self.fundo
	
	def Login(self):
		def FuncaoEntrar():
			#importar arquivo
			pass
		
		def FuncaoCadastrar():
			self.janela.destroy()
			c = Cadastro()
			c.Cadastrar()	

		self.janela.geometry("270x230+800+200")
		self.janela.title("Boletim - Login")

		self.textoLogin = Label(self.janela, text="Login:", font= "arial, 16", bg= self.fundo, fg="light green")
		self.entradaLogin = Entry(self.janela)
		self.textoSenha = Label(self.janela, text="Senha:", font= "arial, 16", bg= self.fundo, fg="light green")
		self.entradaSenha = Entry(self.janela, show="•")
		self.botaoEntrar = Button(self.janela, text="Entrar", command= FuncaoEntrar)
		self.botaoCadastrar = Button(self.janela, text="Cadastrar", command = FuncaoCadastrar)
		

		self.textoLogin.place(x= 10, y =60)
		self.entradaLogin.place(x= 80, y =67)
		self.textoSenha.place(x= 9, y =100)
		self.entradaSenha.place(x= 80, y =107)
		self.botaoEntrar.place(x= 120, y =150)
		self.botaoCadastrar.place(x= 110, y= 180)
		self.janela.mainloop()

class Cadastro():
	def __init__(self,janela=Tk ):
		self.janela = janela()
		self.janela.resizable(0,0)
		self.fundo = "black"
		self.janela["background"] = self.fundo

	def Cadastrar(self):
		
		def FuncaoVoltar():
			self.janela.destroy()
			c = TelaPrincipal(Tk())
			c.Login()

		self.janela.geometry("300x250+800+200")
		self.janela.title("Boletim - Cadastro")

		self.textoLogin = Label(self.janela, text="Login:", font= "Helvetica, 16", bg= self.fundo, fg="light green")
		self.entradaLogin = Entry(self.janela)
		self.textoConfirmarSenha = Label(self.janela, text="Confirmar:", font= "Helvetica, 16", bg= self.fundo, fg="light green")
		self.entradaConfirmarSenha = Entry(self.janela, show="•")
		self.textoSenha = Label(self.janela, text = "Senha:", font = "Helvetica, 16", bg = self.fundo, fg = "light green")
		self.entradaSenha = Entry(self.janela)
		self.textoMatricula = Label(self.janela, text="Matricula:", font = "Helvetica, 16", bg = self.fundo, fg = "light green")
		self.entradaMatricula = Entry(self.janela)

		self.botaoCadastrar = Button(self.janela, text="Cadastrar")
		self.botaoVoltar = Button(self.janela, text = "Voltar", command= FuncaoVoltar)


		self.textoLogin.place(x= 10, y =60)
		self.entradaLogin.place(x= 108, y =67)
		self.textoSenha.place(x= 9, y =100)
		self.entradaSenha.place(x= 108 , y =107)
		self.textoConfirmarSenha.place(x = 8, y = 140)
		self.entradaConfirmarSenha.place(x = 108, y = 147)
		self.textoMatricula.place(x = 7, y = 180)
		self.entradaMatricula.place(x = 108, y = 187)

		self.botaoCadastrar.place(x= 85, y= 220)
		self.botaoVoltar.place(x = 155, y = 220)
		

if __name__ == '__main__':
	tela = TelaPrincipal(Tk())
	tela.Login()
from tkinter import *

class Boletim:

	def __init__(self, janela):
		self.materias = ["Biologia", "Ed. Física","Artes","Filosofia","Física","Geografia","História","Informática","Programação", "português", "Matemática","MMCP","Química","Sociologia"]
		self.n1 = ["10","10","10","10","10","10","10","10","10","10","10","10","10","10"]
		self.n2 = self.n1[:]
		self.r1 = ["-" for x in range(14)]
		self.n3 = self.n1[:]
		self.n4 = self.n1[:]
		self.r2 = ["-" for x in range(14)]
		self.rf = ["-" for x in range(14)]
		self.nf = self.n1[:]
		self.nomes = ["materias", "n1", "n2", "r1", "n3", "n4", "r2", "rf", "nf"]
		self.janela = janela
		self.janela.title('Boletim')
		self.janela.geometry("450x600+450+70")

	def user(self):
		c.info_cadastro()
		#Label

	def labels(self):
		Label(self.janela, text= self.nomes[0]).place(x= 10, y = 100)
		x = 85
		for palavra in self.nomes[1:]:
			x += 40
			Label(self.janela, text= palavra).place(x = x, y = 100)



	def Materias(self):
		Label(self.janela, text= self.materias[0]).place(x= 10, y = 140)
		x = 10
		y = 140

		for palavra in self.materias[1:]:
			y += 40
			Label(self.janela, text= palavra).place(x = 10, y = y)

	def notas1(self):
		x = 128
		y = 140
		Label(self.janela, text= self.n1[0]).place(x= x, y = y)

		for palavra in self.n1[1:]:
			y += 40		
			Label(self.janela, text= palavra).place(x = x, y = y)


	def notas2(self):
		x = 168
		y = 140
		Label(self.janela, text= self.n2[0]).place(x= x, y = y)
		
		for palavra in self.n2[1:]:
			y += 40		
			Label(self.janela, text= palavra).place(x = x, y = y)

	def notasR1(self):
		x = 208
		y = 140
		Label(self.janela, text= self.r1[0]).place(x= x, y = y)
		
		for palavra in self.r1[1:]:
			y += 40		
			Label(self.janela, text= palavra).place(x = x, y = y)

	def notas3(self):
		x = 248
		y = 140
		Label(self.janela, text= self.n3[0]).place(x= x, y = y)
		
		for palavra in self.n3[1:]:
			y += 40		
			Label(self.janela, text= palavra).place(x = x, y = y)

	def notas4(self):
		x = 288
		y = 140
		Label(self.janela, text= self.n4[0]).place(x= x, y = y)
		
		for palavra in self.n4[1:]:
			y += 40		
			Label(self.janela, text= palavra).place(x = x, y = y)

	def notasR2(self):
		x = 328
		y = 140
		Label(self.janela, text= self.r2[0]).place(x= x, y = y)
		
		for palavra in self.r2[1:]:
			y += 40		
			Label(self.janela, text= palavra).place(x = x, y = y)

	def notasRf(self):
		x = 368
		y = 140
		Label(self.janela, text= self.rf[0]).place(x= x, y = y)
		
		for palavra in self.rf[1:]:
			y += 40		
			Label(self.janela, text= palavra).place(x = x, y = y)

	def notasNf(self):
		x = 408
		y = 140
		Label(self.janela, text= self.nf[0]).place(x= x, y = y)
		
		for palavra in self.nf[1:]:
			y += 40		
			Label(self.janela, text= palavra).place(x = x, y = y)


		
		self.janela.mainloop()




if __name__ != "__main__":
	a = Boletim(Tk())
	a.labels()
	a.Materias()
	a.notas1()
	a.notas2()
	a.notasR1()
	a.notas3()
	a.notas4()
	a.notasR2()
	a.notasRf()
	a.notasNf()

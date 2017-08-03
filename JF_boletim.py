#criando escola
class Escola():
	def __init__(self,nome,endereco,campus):
		self.nome = nome
		self.endereco = endereco
		self.campus = campus
		self.cursos = ["Informática","Mecânica","Edificações","Estradas","Química","Eletrônica","Eletrotécnica"]

	def info_escola(self):
		print("----- Dados Escola ----")
		print("Nome: %s\nEndereço: %s\nCampus: %s\n\n--- Cursos ---\n" % (self.nome,self.endereco,self.campus))
		for x in self.cursos:
			print(x)
		print("-----------------------")

#cirando pessoa
class Pessoa(object):
	def __init__(self,nome,cpf,idade,endereco,telefone):
		self.nome = nome
		self.cpf = cpf
		self.idade = idade
		self.endereco = endereco
		self.telefone = telefone

#criando aluno
class Aluno(Pessoa):
	def __init__(self,nome,cpf,idade,endereco,telefone):
		Pessoa.__init__(self,nome,cpf,idade,endereco,telefone)

	def info_aluno(self):
		print("----- Dados Aluno -----")
		print("Nome: %s\nCPF: %s\nIdade: %d\nEndereço: %s\nTelefone: %d" % (self.nome,self.cpf,self.idade,self.endereco,self.telefone))
		print("-----------------------")
		
#criando responsavel
class Responsavel(Pessoa):
	def __init__(self,nome,cpf,idade,endereco,telefone,parentesco):
		Pessoa.__init__(self,nome,cpf,idade,endereco,telefone)
		self.parentesco = parentesco

	def info_responsavel(self):
		print("-- Dados Responsável --")
		print("Nome: %s\nCPF: %s\nIdade: %d\nEndereço: %s\nTelefone: %d\nParentesco: %s" % (self.nome,self.cpf,self.idade,self.endereco,self.telefone,self.parentesco))
		print("-----------------------")
		

#criando cadastro
class Cadastro(Aluno):
	def __init__(self):
		self.lista_dados = []
		#self.curso_esc = e.cursos
		#print(self.curso_esc)


	def cadastrando(self,nome,cpf,idade,curso,serie,endereco,telefone):
		self.curso = curso
		self.serie = serie
		Aluno.__init__(self,nome,cpf,idade,endereco,telefone)
		self.lista_dados.append(self.nome)
		self.lista_dados.append(self.cpf)
		self.lista_dados.append(self.idade)
		self.lista_dados.append(self.curso)
		self.lista_dados.append(self.serie)
		self.lista_dados.append(self.endereco)
		self.lista_dados.append(self.telefone)
		
		if len(self.lista_dados) == 7:
			pass
		else:
			print("Faltando dados!")

	
	
	def info_cadastro(self,a="Cadastro"):
		print("-- Dados do",a,"--")
		print("Nome: %s\nCPF: %s\nIdade: %d\nCurso: %s\nSérie: %s\nTelefone: %d\nEndereço: %s" % (self.nome,self.cpf,self.idade,self.curso,self.serie,self.telefone,self.endereco))
		print("-----------------------")

#criando login				
class Login():
	def __init__(self):
		self.nome = c.nome
		self.senha = c.cpf
		self.info_do_cadastrado = list()
	

	def logando(self,user_login,senha_login):

		self.user_login = user_login
		self.senha_login = senha_login

		if self.user_login == self.nome:
			if self.senha_login == self.senha:
				print("\nSeja muito Bem-vindo %s " %(self.user_login))
				self.info_do_cadastrado.append(c.info_cadastro(a="Cadastrado"))

			else:
				print("Senha incorreta!")
		else: 
			print("Dados incorretos!")

class Boletim():
	def __init__(self):
		self.dados = list()
		self.dados.append(c.info_cadastro())
		print(self.dados)
		

	def criando_bol(self):
		import bol






if __name__ == '__main__':
	e = Escola("IFAL","Rua Mizael Domingues, 75","Maceió")
	e.info_escola()
	a = Aluno("José Fernandes","058.527.453-32", 16,"Rua João Monteiro Silva",993478480)
	a.info_aluno()
	r = Responsavel("Deyvisson","11111111111",21,"Rua João Monteiro Silva",993478480,"Irmão")
	r.info_responsavel()
	c = Cadastro()
	c.cadastrando("José Fernandes","058.527.453-32", 16,"Informática","2º ano","Rua João Monteiro Silva",993478480)
	c.info_cadastro()
	l = Login()
	l.logando("José Fernandes","058.527.453-32"	)
	b = Boletim()
	b.criando_bol()
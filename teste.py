class Conta:

	def __init__(self, titular, agencia, numero, saldo_inicial):
		self.__titular = titular
		self.__agencia = agencia
		self.__numero = numero
		self.__saldo = saldo_inicial
		self.__ativa = False
		self.__operaçoes = [('saldo inicial', saldo_inicial)]
		pass
	
	@property
	def titular(self):
		return self.__titular

	@property
	def agencia(self):
		return self.__agencia
	
	@property
	def numero(self):
		return self.__numero
	
	@property
	def saldo(self):
		return self.__saldo
	
	@property
	def ativa(self):
		return self.__ativa
	
	@ativa.setter
	def ativa(self, situacao):
		if isinstance(situacao, bool) == True:
			self.ativa = situacao
		pass
	
	def depositar(self, valor):
		if valor > 0 and self.ativa == True:
			self.__saldo += valor
			print(f'Deposito realizado. Saldo: R$ {self.__saldo}')
			self.__operaçoes.append('deposito', valor)
			pass

	def sacar(self, valor):
		if valor > self.__saldo or valor <= 0 :
			return(f'Saque falhou. Saldo: R$ {self.__saldo}')
		if self.__ativa == True:
			self.__saldo -= valor
			print(f'Saque realizado. Saldo: R$ {self.__saldo}')
			self.__operaçoes.append('saque', valor)
			return valor
		pass

	def transferir(self, conta_destino, valor):
		pass

	def tirar_extrato(self):
		return self.__operaçoes

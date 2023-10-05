from transaction.transaction import *

class account(transaction):
	def __init__(self, *args):
		#print(args)
		if (len(args) == 1):
			try: 
				if (args)[0] < 0.0:
					raise ValueError("Balance is less than zero.")
			except ValueError as e:
					exit(e)
			finally:
				self.__balance = float(args[0]) # This is a private instance varianle
				self.public = 'public'  # This is a public instance variable
				self._protected = 'protected' # This is a protected instance variable
		else:
			self.__balance = 0.0

	def __privateMethod(self):
		print('Private Method')

	def _protectedMethod(self):
		print('Protected Method')

	def publicMethod(self):
		print('Public Method')
	
	""" def __del__(self):
		print('Account Destroyed') """
	
	def getBalance(self):
		return self.__balance
	
	def isEmpty(self):
		return self.__balance == 0
	
	def credit(self, amount: float):
		try:
			if (amount < 0.0):
				raise ValueError("Credit amount is less than zero")
		except ValueError as e:
			exit(e)
		else:
			self.__balance += amount

	def debit(self, amount: float):
		try:
			if (amount < 0.0):
				raise ValueError("Debit amount is less than zero.")
			if (amount > self.__balance):
				raise ValueError("Debit amount is greater than the balance.")
		except ValueError as e:
			exit(e)

		self.__balance -= amount
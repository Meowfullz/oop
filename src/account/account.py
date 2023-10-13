from transaction.transaction import *

class account(transaction):
	"""The account class includes  methods to manage the balance of a banking account

	Args:
		transaction (transaction): abstract class that defines methods that
		may be implemented by an account class
	"""	
	def __init__(self, *args):
		"""constructs an account with a specified balance if args length is 1, else constructs an
		account with a balance of 0

		Raises:
			ValueError: indicates args[0] is less than 0
		"""		
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
			self.public = 'public'  # This is a public instance variable
			self._protected = 'protected' # This is a protected instance variable

	def __privateMethod(self):
		print('Private Method')

	def _protectedMethod(self):
		print('Protected Method')

	def publicMethod(self):
		print('Public Method')
	
	""" def __del__(self):
		print('Account Destroyed') """
	
	def getBalance(self):
		"""Prints the balance of the calling account 

		Returns:
			float: the balance
		"""		
		return self.__balance
	
	def isEmpty(self):
		"""checks if the balance of the calling account is 0

		Returns:
			boolean: True if the balance for the calling is 0, else False
		"""		
		return self.__balance == 0
	
	def credit(self, amount: float):
		"""Increases the balance of the calling account by the specified amount 

		Args:
			amount (float): the amount to increase the balance by

		Raises:
			ValueError: indicates the specified amount is less than 0
		"""		
		try:
			if (amount < 0.0):
				raise ValueError("Credit amount is less than zero")
		except ValueError as e:
			exit(e)
		else:
			self.__balance += amount

	def debit(self, amount: float):
		"""Decreases the balance of the calling account by the specified amount

		Args:
			amount (float): amount to decrease the balance by

		Raises:
			ValueError: indicates the specified amount is less than 0
			ValueError: indicates the amount is greate than the balance of the calling account
		"""		
		try:
			if (amount < 0.0):
				raise ValueError("Debit amount is less than zero.")
			if (amount > self.__balance):
				raise ValueError("Debit amount is greater than the balance.")
		except ValueError as e:
			exit(e)
		else:
			self.__balance -= amount

	def __str__(self):
		"""Returns the string representation of the account specified

		Returns:
			str: string representation of the specified account
		"""		
		return f"Account balance={self.__balance} public={self.public}"
	
	def __eq__(self, other):
		"""Tests to see if calling account is equal to the specified object

		Args:
			other: The account specified

		Returns:
			Boolean: returns true if the specified accounts are equal, False if not
		"""		
		# check if other is not none
		if other is not None:
			# check if other is an account type
			if isinstance(other,account):
				# check if others balance is equal to the balance
				# of the calling object
				if other.__balance == self.__balance:
					return True
		return False
	

	@staticmethod
	def sum(account1, account2):
		"""Adds the balances of the two accounts specified as long as the objects are not null

		Args:
			account1 (account): account object 1
			account2 (account): account object 2

		Returns:
			float: Returns the sum of the two accounts if not null, if null returns 0.0
		"""		
		if(account1 is None or account2 is None):
			return 0.0
		elif (not isinstance(account1, account) or not isinstance(account2, account)):
			return 0.0
		else:
			return account1.__balance + account2.__balance
		
	@staticmethod
	def transfer(a, amount:float):
		"""Transfers a specified amount of funds to a new account, and debits the amount from the specified
		account object

		Args:
			a (account): Account to be Debited
			amount (float): Debit amount

		Raises:
			ValueError: indicates amount is less than 0
			ValueError: indicates ammount is none
			ValueError: indicates account is not an account type
			ValueError: indicates the debit amount is greater than the balance in the specified amount 
			object to be debited

		Returns:
			account: new account object
		"""		
		try:
			if (amount < 0.0):
				raise ValueError("Debit amount is less than zero")
			elif (a is None):
				raise ValueError("Account is None")
			elif(not isinstance(a, account)):
				raise ValueError ("a is not an account type")
			elif (amount > a.getBalance()):
				raise ValueError("Debit amount is greater than the balance in the specified account.")
		except ValueError as e:
			exit(e)
		else: 
			a.debit(amount)
			newAccount = account(amount)
			return newAccount

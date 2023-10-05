from abc import ABC, abstractmethod

class transaction:
	"""The transaction abstract class defines methods that may be 
	implemented by an Account class
	"""	
	@abstractmethod
	def getBalance(self):
		"""Returns the current balance of this account
		"""		
		pass


	@abstractmethod
	def isEmpty(self):
		"""Checks if the balance for this account is zero and returns True
		if the balance is zero, else returns false
		"""		
		pass


	@abstractmethod
	def credit(self, amount: float):
		"""Increases the balance of this account by a specific amount

		Args:
			amount (float): the amount to increase the ballance by
		"""		
		pass

	@abstractmethod
	def debit(self, amount: float):
		"""Decreases the balance of this account by the speifc amount

		Args:
			amount (float): the amount to decrease the balance by
		"""		
		pass



	
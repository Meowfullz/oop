from account.account import *
class savingsaccount(account):
	"""The savings account class has methods to to manage the specified accounts balance and 
	interest rate of a savings account

	Args:
		account (account): class that includes methods to change balance and interest rate
	"""
	def __init__(self, balance, interestRate):
		"""constructs the savings account with a specified balance and interest rate

		:ivar __balance: balance of this account
		:ivar __interestRate: interest rate of this account

		Args:
			balance (float): Balance of the account
			interestRate (float): Interest Rate
		"""		
		super().__init__(balance)
		self.__interestRate = interestRate

	def setInterestRate(self, interestRate: float):
		"""Sets interest rate for the specified account

		Args:
			interestRate (float): interest rate
		"""		
		self.__interestRate = interestRate

	def getInterestRate(self):
		"""Returns the Interest Rate for the specified account

		Returns:
			float: Interest Rate
		"""		
		return self.__interestRate
	
	def getInterest(self):
		"""Returns the amount of interest an account has accrued

		Returns:
			float: interest
		"""		
		return self.getBalance() * self.__interestRate
	
	def credit(self, amount:float):
		"""Increases balance of the specified account by the specified amount and 
		times it by the interest rate of the specified savings account

		Args:
			amount (float): amount to increase the balance by
		"""		
		super().credit(amount * self.__interestRate)

	def __str__(self):
		"""Returns the string representation of the calling savings account

		Returns:
			str: string representation of the calling savings account
		"""		
		return f"savings account balance={self.getBalance()} interestRate={self.__interestRate}"
	
	def __eq__(self, other):
		"""Tests if the savings account is equal to the specified object, if nor returns False

		Args:
			other: specified object

		Returns:
			boolean: If the calling savings account is equal to the specified object, returns true. 
			Returns False if not
		"""		
		if other is not None:
			if isinstance(other, savingsaccount):
				if other.getBalance() == self.getBalance():
					if other.__interestRate == self.__interestRate:
						return True
		return False

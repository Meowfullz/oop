from account.account import *
from savingsaccount.savingsaccount import *
def main():
	# Create an account object named a1 that has a balance of $100
	
	a1 = account(100.0)
	a2 = account()
	# a1 = account(100.0, 200.0, 300.0, 400.0)
	# a1 = account(-100.0) a balance less than zero will result in the code raising a valueerror

	#print(a1.public) referencing  a public instnce variabe will not result in an error
	#print(a1.__balance) referencing a private instance variable will result in an error
	# print(a1._protected) referencing a protected instance variable will not result in an error
	# print(a1._account__balance)

	# a1.__privateMethod() referencing a private instance method will result in an error
	# a1._account__privateMethod()
	# a1._protectedMethod() referencing a protected method will not result in an error
	# a1.publicMethod()  referencing a public method will not result in an error


	# display the balance of a1
	print("$%.2f" % (a1.getBalance()))

	# increase the balance of a1 by $50
	a1.credit(50.0)
	# a1.credit(-50.0)

	# display the balance of a1
	print("$%.2f" % (a1.getBalance()))

	#decrease the balance of a1 by $75
	a1.debit(75.0)
	# a1.debit(-75.0)
	# a1.debit(151.0)

	# display the balance of a1
	print("$%.2f" % (a1.getBalance()))

	# display if the balance of a1 is empty
	print('Is a1 empty?', a1.isEmpty())

	#create a second account object named a2 and initilize
	# it balance to zero
	a2 = account()

	# display the balance  of a2
	print("$%.2f" % (a2.getBalance()))

	# increase the balance of a2 by $50
	a2.credit(150.0)

	# display the balance of a2
	print("$%.2f" % (a2.getBalance()))

	# decrease the balance of a2 by $75
	a2.debit(75.0)

	# display the balance of a2
	print("$%.2f" % (a2.getBalance()))

	# display if the balance of a2 is empty
	print('Is a1 empty?', a2.isEmpty())

	# display a string representation of a1 and a2
	print(a1)
	print(a2)

	# create an object named a3 that is equal to None
	a3  = None

	#test if a1 is equal to a3
	print('Is a1 equal to a3?', a1.__eq__(a3))

	# create a string object named s1
	s1 = "Test"

	# test if a1 is equal to s1
	print('Is a1 equal to s1', a1.__eq__(s1))

	# test if a1 is equal to a2
	print('Is a1 equal to a2', a1.__eq__(a2))

	# change the balance in a2
	a2.credit(75.0)

	# test if a1 is equal to a2
	print('Is a1 equal to a2', a1.__eq__(a2))

	#  display the sum of the balances in a1 and a2
	print("$%.2f" % account.sum(a1, a2))

	#display the sum of balances in a1 and a3
	print("$%.2f" % account.sum(a1, a3))

	# display the sum of balances in a1 and s1
	print("$%.2f" % account.sum(a1, s1))
	

	#transfer $25 out of a1 and put it into a new account named a4
	a4 = account.transfer(a1, 25.0)
	# a4 = account.transfer(a1, -25.0) - Results in ValueError
	# a4 = account.transfer(a1, 2500.0) Results in Value Error
	# a4 = account.transfer(a3, 25.0)
	# a4 = account.transfer(s1, 25.0)
	# display the balances in a1 and a4
	print("Balance in a1 $%.2f" % (a1.getBalance()))
	print("Balance in a4 $%.2f" % (a4.getBalance()))

	
	#create a savings account object named sa1 and initialize 
	#its balance to $10000 and its interest rate to 6%
	sa1 = savingsaccount(10000.0, .06)

	#display the balance of sa1
	print("Balance in sa1: $%.2f" % (sa1.getBalance()))

	#display the interest rate of sa1
	print("Interest Rate: %.2f" % (sa1.getInterest()))

	# display if the balance of sa1 is empty
	print("Is sa1 empty? ", sa1.isEmpty()) 

	# display a string representation of sa1
	print(sa1)

	# is sa1 equal a1
	print("Is sa1  equal to a3", sa1.__eq__(a1))

	# is sa1 equal to a3
	print("Is sa1  equal to a3", sa1.__eq__(a3))

	sa2=savingsaccount(10000.0, 0.05)

	print("Is sa1  equal to sa2", sa1.__eq__(sa2))

	#change the interest rate of sa2 to 6%
	sa2.setInterestRate(.06)

	print("Is sa1  equal to sa2", sa1.__eq__(sa2))

	# credit sa2 by 1000
	sa2.credit(1000.0)

	#display the balance of sa2
	print("Balance in sa2: $%.2f" % (sa2.getBalance()))

	# debit sa2 by $1000
	sa2.debit (1000.0)
	
	#display the balance of sa2
	print("Balance in sa2: $%.2f" % (sa2.getBalance()))



if __name__ == "__main__":
	main()
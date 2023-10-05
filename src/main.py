from account.account import *
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


if __name__ == "__main__":
	main()
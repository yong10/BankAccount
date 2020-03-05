class BankAccount:
	def __init__(self, int_rate, balance):
		self.int_rate = int_rate
		self.balance = balance
	
	def deposit(self, amount):
		self.balance += amount
		return self
	
	def withdraw(self, amount):
		if self.balance >= amount:
			self.balance -= amount
		else:
			print("Insufficient funds: Charging a $5 fee")
			self.balance -= 5
		return self
	
	def display_account_info(self):
		print(f"Balance: ${self.balance}")
		return self

	def yield_interest(self):
		if self.balance > 0:
			self.balance += self.balance * self.int_rate
		return self
	


BankAccount1 = BankAccount(0.10, 0)
BankAccount1.deposit(100).deposit(100).deposit(100).withdraw(50).yield_interest().display_account_info()

BankAccount2 = BankAccount(0.10, 0)
BankAccount2.deposit(100).deposit(100).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()
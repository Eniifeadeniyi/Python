def deposit(amount, balance = 0, transactions = []):
	if type(amount) == float or type(amount) == int:
		if amount > 0:
			balance += amount
		if amount < 0:
			print("Invalid amount!")
	else:
		print("Invalid input!")
	transaction = f"Deposited : {amount} | Balance: {balance}"
	transactions.append(transaction)
	return balance,transactions

def withdraw(amount,balance = 0, transactions = []):
	if type(amount) == float or type(amount) == int:
		if amount <= balance: 
			balance -= amount
		else:
			print("Withdrawal failed: insufficient funds")
		
	else:
		print("Invalid input!")
	transaction = f"Withdrew : {amount} | New Balance : {balance}"
	transactions.append(transaction)
	return balance,transactions

def history(transactions):
	for transaction in transactions:
		print(transaction)
	if transactions == []:
		print("No transactions made yet")






def get_deposit(amount, balance = 0, transactions = []):
	if amount > 0:
		balance += amount
		return balance
	return "Invalid input!"



def make_withdrawal(amount, balance = 0, transactions = []):
	if amount > balance :
		print("Withdrawal failed: insufficient funds")
	if amount <= balance:
		balance -= amount
	return balance


def show_transaction_history(transactions = []):
	for transaction in transactions:
		print(transaction)
	if transactions == []:
		print("No transactions yet")
def get_deposit(amount, balance = 0, transactions = []):
	balance += amount
	transaction = f"Deposited : {amount} | New Balance : {balance} "
	transactions.append(transaction)
	return balance



def make_withdrawal(amount, balance = 0, transactions = []):
	if amount > balance :
		print("Withdrawal failed: insufficient funds")
	if amount <= balance:
		balance -= amount
	transaction = f"Withdrew : {amount} | New Balance : {balance}"
	transactions.append(transaction)
	return balance



def show_transaction_history(transactions):
	if transactions == []:
		print("No transactions yet.")
	return transactions
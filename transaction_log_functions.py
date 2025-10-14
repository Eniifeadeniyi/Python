def get_deposit(amount, balance, transactions):
	balance += amount
	transactions += f"Deposited : {amount} | New Balance : {balance} "
	return f'Your new balance is: {balance}'



def make_withdrawal(withdraw, balance, transactions):
	if withdraw > balance :
		print("Withdrawal failed: insufficient funds")
	if withdraw <= balance:
		balance -= withdraw
	transactions += f"Withdrew : {withdraw} | New Balance : {balance}"
	return f'Your new balance is: {balance}'



def show_transaction_history(transactions):
	if transactions == "":
		print("No transactions yet.")
	return transactions
from transaction_log_functions import *

balance = 0.00
transactions = []
print("Welcome to Transaction Log App")
choice = 0
while choice != 4:
	menu = """
	1. Deposit
	2. Withdraw
	3. Show Transactions
	4. Exit	
		"""
	print(menu)
	choice = int(input("Enter your choice: "))
	match choice:
		case 1: 
			deposit = float(input("Enter deposit amount: "))
			if deposit > 0:
				balance = get_deposit(deposit, balance)
				transaction = f"Deposited : {deposit} | New Balance : {balance}"
				transactions.append(transaction)
				print("New balance: " + str(balance))
			print(get_deposit(deposit))

		case 2: 
			withdraw = float(input("Enter withdraw amount: "))
			balance = make_withdrawal(withdraw, balance)
			transaction = f"Withdrew : {withdraw} | New Balance : {balance}"
			transactions.append(transaction)
			print("New balance is: " + str(balance))
	
		case 3: 
			transactions = show_transaction_history(transactions)

		case 4:
			print("Final balance: " + str(balance))
			transactions = show_transaction_history(transactions)


		case _: print("Please enter a number above")
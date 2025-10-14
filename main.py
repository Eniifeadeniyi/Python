from transaction_log_functions import*

balance = 0.00
transactions = ""
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
			deposit = int(input("Enter deposit amount: "))
			print(get_deposit(deposit, balance, transactions))

		case 2: 
			withdraw = int(input("Enter withdraw amount: "))
			print(make_withdrawal(withdraw, balance, transactions))
	
		case 3: 
			print(show_transaction_history(transactions))

		case 4:
			print(balance)
			print(show_transaction_history(transactions))

		case _: print("Please enter a number above")
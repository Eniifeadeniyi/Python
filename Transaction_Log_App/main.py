from transaction_functions import *

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
	choice = input("Enter your choice: ")
	match choice:
		case "1": 
			amount = float(input("Enter deposit amount: "))
			balance,transactions = deposit(amount,balance)	
			print("New balance: " + str(balance))

		case "2": 
			amount = float(input("Enter withdraw amount: "))
			balance, transactions = withdraw(amount,balance,transactions)	
			print("New balance is: " + str(balance))
	
		case "3": 
			history(transactions)
			
		case "4" :
			print("Final balance: " + str(balance))
			history(transactions)
			print("Thank you for using the Transaction Log App!")
			break
			
		case _: print("Please, enter a number from the list below: ")

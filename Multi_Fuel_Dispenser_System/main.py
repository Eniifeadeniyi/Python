from functions import *

receipts = []

menu = """
	Welcome to Eniife's Station!
	1. Buy Petroleum
	2. Show Transaction History
	3. Exit
	"""
print(menu)


main = """
	Petroleum Options:
		1. Petrol => #1000/liter
		2. Diesel => #1500/liter
		3. Kerosene => #1200/liter
		4. Gas => #1800/liter
		"""


operation = input("Enter operation: ")
while operation != 3:
	match operation:
		case "1" : 
			print(main)
			option = input("Enter operation: ")
			match option:
				case "1" :
					choice = input("Liter or Amount: ").lower();
					match choice:
						case "amount" :
							amount = float(input("How much Petrol are you buying(1000/L): "))
							amount, number_of_litres = petrol_amount(amount)
							print(format_petrol_amount_receipt(amount,number_of_litres))
							receipts.append(format_petrol_liter(liter,price))
							
						
						case "liter" :
							liter = float(input("How many liters of Petrol are you buying(1000/L): "))
							price, liter = petrol_liter(liter)
							print(format_petrol_liter(liter,price))
							receipts.append(format_petrol_liter(liter,price))
							

				case "2" :
					choice = input("Liter or Amount: ").lower();
					match choice:
						case "amount" :
							amount = float(input("How much Petrol are you buying(1000/L): "))
							amount, number_of_litres = diesel_amount(amount)
							print(format_diesel_amount_receipt(amount,number_of_litres))
							receipts.append(format_diesel_amount_receipt(amount,number_of_litres)))
							
						
						case "liter" :
							liter = float(input("How many liters of Petrol are you buying(1000/L): "))
							price, liter = diesel_liter(liter)
							print(format_diesel_liter(liter,price))
							receipts.append(format_diesel_liter(liter,price))


		case "2" :
			show_history(receipts)
		case "3" : 
			print("See you later!!!")
		case _: 
			print("Kindly, enter a number from below:")


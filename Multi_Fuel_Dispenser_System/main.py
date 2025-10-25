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
							print("Customer's Transaction Receipt")
							print(format_petrol_amount_receipt(amount,number_of_litres))
							print("Saving Transaction History...")
							receipts.append(format_petrol_amount_receipt(amount,number_of_litres))
							
						
						case "liter" :
							liter = float(input("How many liters of Petrol are you buying(1000/L): "))
							price, liter = petrol_liter(liter)
							print("Customer's Transaction Receipt")
							print(format_petrol_liter_receipt(liter,price))
							print("Saving Transaction History...")
							receipts.append(format_petrol_liter_receipt(liter,price))
							

				case "2" :
					choice = input("Liter or Amount: ").lower();
					match choice:
						case "amount" :
							amount = float(input("How much Petrol are you buying(1000/L): "))
							amount, number_of_litres = diesel_amount(amount)
							print("Customer's Transaction Receipt")
							print(format_diesel_amount_receipt(amount,number_of_litres))
							print("Saving Transaction History...")
							receipts.append(format_diesel_amount_receipt(amount,number_of_litres))
							
						
						case "liter" :
							liter = float(input("How many liters of Petrol are you buying(1000/L): "))
							price, liter = diesel_liter(liter)
							print("Customer's Transaction Receipt")
							print(format_diesel_liter_receipt(liter,price))
							print("Saving Transaction History...")
							receipts.append(format_diesel_liter_receipt(liter,price))
				case "3" :
					choice = input("Liter or Amount: ").lower();
					match choice:
						case "amount" :
							amount = float(input("How much Petrol are you buying(1000/L): "))
							amount, number_of_litres = kerosene_amount(amount)
							print("Customer's Transaction Receipt")
							print(format_kerosene_amount_receipt(amount,number_of_litres))
							print("Saving Transaction History...")
							receipts.append(format_kerosene_amount_receipt(amount,number_of_litres))
							
						
						case "liter" :
							liter = float(input("How many liters of Petrol are you buying(1000/L): "))
							price, liter = kerosene_liter(liter)
							print("Customer's Transaction Receipt")
							print(format_kerosene_liter_receipt(liter,price))
							print("Saving Transaction History")
							receipts.append(format_kerosene_liter_receipt(liter,price))


				case "4" :
					choice = input("Liter or Amount: ").lower();
					match choice:
						case "amount" :
							amount = float(input("How much Petrol are you buying(1000/L): "))
							amount, number_of_litres = gas_amount(amount)
							print("Customer's Transaction Receipt")
							print(format_gas_amount_receipt(amount,number_of_litres))
							print("Saving Transaction History")
							receipts.append(format_gas_amount_receipt(amount,number_of_litres))
							
						
						case "liter" :
							liter = float(input("How many liters of Petrol are you buying(1000/L): "))
							price, liter = gas_liter(liter)
							print("Customer's Transaction Receipt")
							print(format_gas_liter_receipt(liter,price))
							print("Saving Transaction History")
							receipts.append(format_gas_liter_receipt(liter,price))




		case "2" :
			show_history()
		case "3" : 
			print("See you later!!!")
		case _: 
			print("Kindly, enter a number from below:")


def petrol_amount(amount, receipts = []):
	if type(amount) == int or type(amount) == float:
		if amount >= 1000:
			number_of_litres = amount / 1000
		else:
			return("Amount must be above a liter price!!!")
	else:
		return("Invalid input!")
	return amount, number_of_litres	

def format_petrol_amount_receipt(amount,number_of_litres):
	return f"""
		Product : Petrol
		Amount : #{amount:.2f}
		Liters : {number_of_litres:.2f}
		Thanks for patronizing Eniife's Station
			Hope to see you again!
		"""


def petrol_liter(number_of_litres, receipts = []):
	if type(number_of_litres) == int or type(number_of_litres) == float:
		if number_of_litres >= 1 and number_of_litres <= 50:
			amount = number_of_litres * 1000
		else:
			return("Liters must be between 1-50!!!")
	else:
		return("Invalid input!")
	return amount,number_of_litres
def format_petrol_liter(number_of_litres,amount):
	return f"""
		Product : Petrol       								
		Amount : #{amount:.2f}  								
		Liters : {number_of_litres:.2f}L   						
		Thanks for patronizing Eniife's Station 			
			Hope to see you again!					
		"""	


def diesel_amount(amount, receipts = []):
	if type(amount) == int or type(amount) == float:
		if amount >= 1500:
			number_of_litres = amount / 1500
		else:
			return("Amount must be above a liter price!!!")
	else:
		return("Invalid input!")
	return amount,number_of_litres

def format_diesel_amount_receipt(amount,number_of_litres):
	return f"""
		Product : Diesel
		Amount : #{amount:.2f}
		Liters : {number_of_litres:.2f}
		Thanks for patronizing Eniife's Station
			Hope to see you again!
		"""
	

def diesel_liter(number_of_litres, receipts = []):
	if type(number_of_litres) == int or type(number_of_litres) == float:
		if number_of_litres >= 1 and number_of_litres <= 50:
			amount = number_of_litres * 1500
		else:
			return("Liters must be between 1-50!!!")
	else:
		return("Invalid input!")
	return amount,number_of_litres	

def format_diesel_liter(number_of_litres,amount):
	return f"""
		Product : Diesel       								
		Amount : #{amount:.2f}  								
		Liters : {number_of_litres:.2f}L   						
		Thanks for patronizing Eniife's Station 			
			Hope to see you again!					
		"""
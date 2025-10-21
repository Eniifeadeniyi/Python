def petrol_amount(amount, receipts = []):
	if type(amount) == int or type(amount) == float:
		if amount >= 1000 and amount <= 50000:
			number_of_litres = amount / 1000
		if amount < 1000:
			return("Amount must be above a liter price!!!")
		if amount > 50000:
			return("You can only purchase a maximum of 50L!!!")
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
		if amount >= 1500 and amount <= 75000:
			number_of_litres = amount / 1500
		if amount < 1500:
			return("Amount must be above a liter price!!!")
		if amount > 75000:
			return("You can only purchase a maximum of 50L!!!")
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


def kerosene_amount(amount, receipts = []):
	if type(amount) == int or type(amount) == float:
		if amount >= 1200 and amount <= 60000:
			number_of_litres = amount / 1200
		if amount < 1200:
			return("Amount must be above a liter price!!!")
		if amount > 60000:
			return("You can only purchase a maximum of 50L!!!")
	else:
		return("Invalid input!")
	return amount,number_of_litres

def format_kerosene_amount_receipt(amount,number_of_litres):
	return f"""
		Product : Kerosene
		Amount : #{amount:.2f}
		Liters : {number_of_litres:.2f}
		Thanks for patronizing Eniife's Station
			Hope to see you again!
		"""
	

def kerosene_liter(number_of_litres, receipts = []):
	if type(number_of_litres) == int or type(number_of_litres) == float:
		if number_of_litres >= 1 and number_of_litres <= 50:
			amount = number_of_litres * 1200
		else:
			return("Liters must be between 1-50!!!")
	else:
		return("Invalid input!")
	return amount,number_of_litres	

def format_kerosene_liter(number_of_litres,amount):
	return f"""
		Product : Kerosene       								
		Amount : #{amount:.2f}  								
		Liters : {number_of_litres:.2f}L   						
		Thanks for patronizing Eniife's Station 			
			Hope to see you again!					
		"""



def gas_amount(amount, receipts = []):
	if type(amount) == int or type(amount) == float:
		if amount >= 1800 and amount <= 90000:
			number_of_litres = amount / 1800
		if amount < 1800:
			return("Amount must be above a liter price!!!")
		if amount > 90000:
			return("You can only purchase a maximum of 50L!!!")
	else:
		return("Invalid input!")
	return amount,number_of_litres

def format_gas_amount_receipt(amount,number_of_litres):
	return f"""
		Product : Gas
		Amount : #{amount:.2f}
		Liters : {number_of_litres:.2f}
		Thanks for patronizing Eniife's Station
			Hope to see you again!
		"""
	

def gas_liter(number_of_litres, receipts = []):
	if type(number_of_litres) == int or type(number_of_litres) == float:
		if number_of_litres >= 1 and number_of_litres <= 50:
			amount = number_of_litres * 1800
		else:
			return("Liters must be between 1-50!!!")
	else:
		return("Invalid input!")
	return amount,number_of_litres	

def format_gas_liter(number_of_litres,amount):
	return f"""
		Product : Gas       								
		Amount : #{amount:.2f}  								
		Liters : {number_of_litres:.2f}L   						
		Thanks for patronizing Eniife's Station 			
			Hope to see you again!					
		"""
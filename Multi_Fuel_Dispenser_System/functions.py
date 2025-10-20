def petrol_amount(amount, receipts = []):
	if type(amount) == int or type(amount) == float:
		if amount >= 1000:
			number_of_litres = amount / 1000
			receipt = f"""
				Product : Petrol       								
				Amount : #{amount:.2f}  								
				Liters : {number_of_litres:.2f}L   						
				Thanks for patronizing Eniife's Station 			
					Hope to see you again!					
		
				"""
		else:
			return("Amount must be above a liter price!!!")
	else:
		return("Invalid input!")
	return receipt	

def petrol_liter(number_of_litres, receipts = []):
	if type(number_of_litres) == int or type(number_of_litres) == float:
		if number_of_litres >= 1 and number_of_litres <= 50:
			amount = number_of_litres * 1000
			receipt = f"""
				Product : Petrol       								
				Amount : #{amount:.2f}  								
				Liters : {number_of_litres:.2f}L   						
				Thanks for patronizing Eniife's Station 			
					Hope to see you again!					
		
				"""
		else:
			return("Liters must be between 1-50!!!")
	else:
		return("Invalid input!")
	return receipt	

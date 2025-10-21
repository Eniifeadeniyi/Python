def get_wage(number_of_deliveries):
	if type(number_of_deliveries) == int:
		if number_of_deliveries >= 0 and number_of_deliveries <= 49:		
			wage = (160 * number_of_deliveries) + 5000
		elif number_of_deliveries >= 50 and number_of_deliveries <= 59:	
			wage = (200 * number_of_deliveries) + 5000
		elif number_of_deliveries >= 60 and number_of_deliveries <= 69:	
			wage = (250 * number_of_deliveries) + 5000
		elif number_of_deliveries >= 70 and number_of_deliveries <= 100:
			wage = (500 * number_of_deliveries) + 5000
		else: return "Invalid input!"
	else: return "Invalid input!"

	return wage
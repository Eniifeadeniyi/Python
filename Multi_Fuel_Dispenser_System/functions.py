def petrol_amount(amount, receipts = []):
	if amount >= 1000:
		number_of_litres = amount / 1000
		receipt = f"""
		=========================================================
		=	Product : Petrol       				=
		=	Amount : #{amount:.2f}  			=
		=	Liters : {number_of_litres:.2f}L   		=
		=	Thanks for patronizing Eniife's Station 	=
		=		Hope to see you again!			=
		=========================================================
		"""
		receipts.append(receipt)
	else:
		return("Amount must be above a liter price!!!")
	return receipt
	
print(petrol_amount(1000))
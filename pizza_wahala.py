guests = int(input("Enter number of guests you are expecting: "))

menu = """
	-------------------------------------------------
	| Pizza Type | Number of slices | Price per box |
	-------------------------------------------------
	| Sapa size  |         4	|      ₦2,500   |
	-------------------------------------------------
	| Small Money|         6        |      ₦2,900   |
	-------------------------------------------------
	| Big boys   |         8	|      ₦4,000   |
	-------------------------------------------------
	| Odogwu     |         12       |      ₦5,200   |
	-------------------------------------------------

""";
print(menu)

pizzaType = input("Enter the pizza type you are interested in: ").lower()

match pizzaType:
	case "sapa size" : 
		numberOfBoxes = guests / 4
		if guests % 4 != 0:
			numberOfBoxes += 1
		
		print("You will need " + str(numberOfBoxes) + " boxes of the sapa size pizza.")

		numberOfSlices = numberOfBoxes * 4
		if numberOfSlices > guests:
			extra = numberOfSlices - guests
			print(str(extra) + " slices will be remanining after serving.")
		
		total = 2500 * numberOfBoxes
		print("Your total charge is ₦" + str(total))

	case "small money" : 
		numberOfBoxes = guests / 6
		if guests % 6 != 0:
			numberOfBoxes += 1
		
		print("You will need " + str(numberOfBoxes) + " boxes of the small money pizza.")

		numberOfSlices = numberOfBoxes * 6
		if numberOfSlices > guests:
			extra = numberOfSlices - guests
			print(str(extra) + " slices will be remanining after serving.")
		
		total = 2900 * numberOfBoxes
		print("Your total charge is ₦" + str(total))



	case "big boys" :
		numberOfBoxes = guests / 8
		if guests % 8 != 0:
			numberOfBoxes += 1
		
		print("You will need " + str(numberOfBoxes) + " boxes of the big boys pizza.")

		numberOfSlices = numberOfBoxes * 8
		if numberOfSlices > guests:
			extra = numberOfSlices - guests
			print(str(extra) + " slices will be remanining after serving.")
		
		total = 4000 * numberOfBoxes
		print("Your total charge is ₦" + str(total))


	case "odogwu" :
		numberOfBoxes = guests / 12
		if guests % 12 != 0:
			numberOfBoxes += 1
		
		print("You will need " + str(numberOfBoxes) + " boxes of the odogwu pizza.")

		numberOfSlices = numberOfBoxes * 12
		if numberOfSlices > guests:
			extra = numberOfSlices - guests
			print(str(extra) + " slices will be remanining after serving.")
		
		total = 5200 * numberOfBoxes
		print("Your total charge is ₦" + str(total))


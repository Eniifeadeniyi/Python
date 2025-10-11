numbers = [1,2,3,4,5,6,7]
	count = 0
	product = 1

	while count < len(numbers) :
		count += 1
		if count % 3 == 0:
			product *= numbers[count]
				
print(product)

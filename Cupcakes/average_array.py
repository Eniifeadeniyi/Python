def average_array(*numbers):
	sum = 0
	count = 0
	for number in numbers:
		sum += number
		count += 1
	average = sum / count
	return average	
print(average_array(1,2,3))
		
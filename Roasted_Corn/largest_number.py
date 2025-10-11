def get_largest_number(*numbers):
	maximum = numbers[0]
	count = 0
	for number in numbers:
		if numbers[count] > maximum:
			maximum = numbers[count]
		count += 1
	return maximum

print(get_largest_number(8,4,9,2,5,6,3))

def get_smallest_number(*numbers):
	minimum = numbers[0]
	count = 0
	for number in numbers:
		if numbers[count] < minimum:
			minimum = numbers[count]
		count += 1
	return minimum

print(get_smallest_number(8,4,9,2,5,6,3))

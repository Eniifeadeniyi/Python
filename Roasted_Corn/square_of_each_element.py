def get_square_of_each_element(*numbers):
	count = 0
	square = []
	while count < len(numbers):
		square.append(numbers[count] ** 2)
		count += 1
	return square
		

print(get_square_of_each_element(2,3,4,5,7))
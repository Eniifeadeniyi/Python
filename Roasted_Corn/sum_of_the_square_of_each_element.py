def get_sum_of_the_square_of_each_element(numbers):
	count = 0
	square = []
	square_sum = 0
	while count < len(numbers):
		square.append(numbers[count] ** 2)
		square_sum += square[count]
		count += 1
	return square_sum

numbers =[2,3,4,5,7]
print(get_sum_of_the_square_of_each_element(numbers))

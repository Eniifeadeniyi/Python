def get_last_element(*numbers):
	if numbers == ( ):
		return 0
	return numbers[len(numbers) - 1]				
print(get_last_element(125,67,89,100))
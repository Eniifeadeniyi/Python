def get_sum_of_specific_elements(*numbers):
	if len(numbers) % 2 != 0:
		middle = (len(numbers) + 1) // 2
		middle = numbers[middle - 1]
	
	if len(numbers) % 2 == 0:
		middle = (len(numbers) + 1) // 2
		middle = (numbers[middle] + numbers[middle - 1]) / 2
	sum = numbers[0] + numbers[-1] + middle 
	return sum
print(get_sum_of_specific_elements(1,2,3,4,5,6))
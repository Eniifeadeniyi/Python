def get_sum_of_every_third_element(*numbers):
	count = 0
	sum = 0

	while count < len(numbers) :
		count += 1
		if count % 3 == 0:
			sum += numbers[count - 1]
	return sum

print(get_sum_of_every_third_element(1,2,3,4,5))

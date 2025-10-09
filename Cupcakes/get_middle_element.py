def get_middle_element(*numbers):
	count = 1
	while count <= len(numbers) :
		count += 1
		if count == len(numbers) :
			if len(numbers) % 2 != 0:
				middle = (len(numbers) + 1) // 2
				middle = numbers[middle]
			if len(numbers) % 2 == 0:
				middle = (len(numbers) + 1) // 2
				middle = numbers[middle - 1]
	return middle
print(get_middle_element(1,2,3,4,5,6,7,8))
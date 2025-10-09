def get_first_element(*numbers):
	count = 0
	if numbers == ( ):
		return 0
	for number in numbers:
		while count < len(numbers):
			count += 1
			if count == 1:
				return number	
	
print(get_first_element(12222,46,789,26))
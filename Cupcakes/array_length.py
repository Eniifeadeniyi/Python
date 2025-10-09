def array_length(*numbers):
	count = 0
	for number in numbers:
		count += 1
	return count
print(array_length(12345420))
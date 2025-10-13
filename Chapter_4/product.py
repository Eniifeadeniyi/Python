def product(*numbers):
	count = 0
	answer = 1
	while count < len(numbers):
		answer *= numbers[count]
		count += 1
	return answer

print(product(1,2,3,4))
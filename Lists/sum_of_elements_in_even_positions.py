numbers = [1,2,3,4,5,6,7]


for number in numbers:
	count = 0
	sum = 0

	while count < len(numbers) :
		if count % 2 == 0:
			sum += numbers[count]
		count += 1
print(sum)
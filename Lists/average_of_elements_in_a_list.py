numbers = [1,2,3,4,5,6,7,8,9,10]

average = 0
sum = 0
count = 0

for number in numbers:
	while count < len(numbers) :
		sum += numbers[count]
		count += 1	
average = sum / count

print(average)
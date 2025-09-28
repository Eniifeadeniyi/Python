total = 0
product = 1

reference_number = int(input("Enter a number: "))
minimum = reference_number
maximum = reference_number

for number in range(3):
	number = int(input("Enter a number: "))
	total = total + number 
	product = product * number

	if(number < minimum):
		minimum = number
	if(number > maximum):
		maximum = number

total += reference_number
product *= reference_number

	
average = total / 4

print("The sum of the numbers entered is: " + str(total))
print("The average of the numbers entered is: " + str(average))
print("The product of the number entered is: " + str(product))
print("The smallest number is: " + str(minimum))
print("The largest number is: " + str(maximum))
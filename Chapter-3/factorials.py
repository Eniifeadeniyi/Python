number = int(input("Enter a number: "))
factorial = 1
counter = 1

while counter <= number:	
	factorial *= counter
	counter = counter + 1
	
print("The factorial of " + str(number) + " is " + str(factorial))


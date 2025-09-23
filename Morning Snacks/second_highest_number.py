first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))
third_number = int(input("Enter your third number: "))

second_maximum = first_number

if second_number < second_maximum:
	if second_number > third_number:
		second_maximum = second_number

if second_number > second_maximum:
	if second_number < third_number:
		second_maximum = second_number

if third_number < second_maximum:
	if third_number > second_number:
		second_maximum = third_number

if third_number > second_maximum:
	if third_number < second_number:
		second_maximum = third_number

print(second_maximum)
number = int(input("Enter a number: "))
counter = 1
maximum = number
second_maximum = number

while counter <= 9:
	next_number = int(input("Enter a number: "))
	counter += 1

	if next_number > maximum:
		second_maximum = maximum
		maximum = next_number

	if next_number > second_maximum and next_number < maximum:
		second_maximum = next_number

print(str(maximum) + " and " + str(second_maximum) + " are the two largest numbers.")
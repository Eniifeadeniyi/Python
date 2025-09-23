"""
	This program is to display the sum, mean, and median of the four numbers.
"""



first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))
third_number = int(input("Enter your third number: "))
fourth_number = int(input("Enter your fourth number: "))

minimum = first_number
if second_number < minimum:
	minimum = second_number
if third_number < minimum:
	minimum = third_number
if fourth_number < minimum:
	minimum = fourth_number

maximum = first_number
if second_number > maximum:
	maximum = second_number
if third_number > maximum:
	maximum = third_number
if fourth_number > maximum:
	maximum = fourth_number

second_maximum = first_number
if second_number < maximum:
	if second_number > second_maximum:
		if second_number < third_number:
			if second_number > fourth_number:
				second_maximum = second_number

if second_number < maximum:
	if second_number > second_maximum:
		if second_number > third_number:
			if second_number < fourth_number:
				second_maximum = second_number

if third_number < maximum:
	if third_number > second_maximum:
		if third_number > second_number:
			if third_number < fourth_number:
				second_maximum = third_number

if third_number < maximum:
	if third_number > second_maximum:
		if third_number < second_number:
			if third_number > fourth_number:
				second_maximum = third_number
if fourth_number < maximum:
	if fourth_number > second_maximum:
		if fourth_number > second_number:
			if fourth_number < third_number:
				second_maximum = fourth_number
if fourth_number < maximum:
	if fourth_number > second_maximum:
		if fourth_number < second_number:
			if fourth_number > third_number:
				second_maximum = fourth_number

second_minimum = first_number
if second_number > minimum:
	if second_number < second_maximum:
		second_minimum = second_number
if third_number > minimum:
	if third_number < second_maximum:
		second_minimum = third_number
if fourth_number > minimum:
	if fourth_number < second_maximum:
		second_minimum = fourth_number

sum = (first_number + second_number + third_number + fourth_number)
mean = sum // 4
median = (second_number + third_number) / 2


print("The mean is: " + str(mean))
print("The sum is: "+ str(sum))
print("The median is: "+ str(median))




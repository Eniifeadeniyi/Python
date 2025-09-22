"""
	Program to arrange 3 numbers from user into ascending order.	
"""

first_number = float(input("Enter your first number: "))
second_number = float(input("Enter your second number: "))
third_number = float(input("Enter your third number: "))

if first_number < second_number and second_number < third_number:
	print(first_number, second_number, third_number)

if second_number < first_number and first_number < third_number:
	print(second_number, first_number, third_number)

if third_number < second_number and second_number < first_number:
	print(third_number, second_number, first_number)

if first_number < third_number and third_number < second_number:
	print(first_number, third_number, second_number)

if second_number < third_number and third_number < first_number:
	print(second_number, third_number, first_number)

if third_number < first_number and first_number < second_number:
	print(third_number, first_number, second_number)

#There are six possible ways the numbers can be arranged: 123, 213, 321, 132, 231, and 312
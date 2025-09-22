"""
  This program calculates and prints the sum, average, product, largest, and smallest of the numbers inputed by the user.
"""

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))

sum = first_number + second_number + third_number
average = sum / 3
product =  first_number * second_number * third_number
smallest = first_number

if second_number < first_number:
  smallest = second_number

if third_number < first_number:
  smallest = third_number


largest = first_number

if second_number > first_number:
  largest = second_number

if third_number > first_number:
  largest = third_number

print("The sum of the numbers is " + str(sum))
print("The average of the numbers is " + str(average))
print("The product of the numbers is " + str(product))
print("The smallest number is " + str(smallest))
print("The largest number is " + str(largest))

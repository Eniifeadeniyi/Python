#ask user to input 3 integers:
#calculate the sum, average, product, smallest number and largest number.
#print sum, average, product, smallest number and largest number.

First_Number = int(input("Enter first number: "))
Second_Number = int(input("Enter second number: "))
Third_Number = int(input("Enter third number: "))

sum = First_Number + Second_Number + Third_Number
average = sum / 3
product =  First_Number * Second_Number * Third_Number
smallest = min(First_Number, Second_Number, Third_Number)
largest = max(First_Number, Second_Number, Third_Number)

print("The sum of the numbers is " + str(sum))
print("The average of the numbers is " + str(average))
print("The product of the numbers is " + str(product))
print("The smallest number is " + str(smallest))
print("The largest number is " + str(largest))

#Ask for user to type in a number.
#Even numbers are divisible by 2, odd numbers are not.
#It should print EVEN if an even number, and ODD if an odd number

number = int(input("Enter a number: "))

if number % 2 == 0:
	print("EVEN")

else: 
	print("ODD")

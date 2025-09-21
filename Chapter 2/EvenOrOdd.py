number = int(input("Enter a number: "))
#Ask for user to type in a number.
#Convert to integer, since input returns as string.

if number % 2 == 0:
	print("EVEN")

else: 
	print("ODD")
#It should print EVEN if an even number, and ODD if an odd number
#Even numbers are divisible by 2, odd numbers are not.

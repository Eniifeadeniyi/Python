# Ask user for input.
# Make sure the user cannot input any number that doesn't have five digits.
# Make each digit in the user's number to be identified singly

number = int(input("Enter a five digit integer: "))


if number > 99999:
	print("Invalid input!")

	if number < 10000:
		print("Invalid input!")
else:
	First_Digit = number // 10000
	Second_Digit = number // 1000 % 10
	Third_Digit = number //100 % 10
	Fourth_Digit = number // 10 % 10
	Fifth_Digit = number % 10

	print(First_Digit, end="   ")
	print(Second_Digit, end="   ")
	print(Third_Digit, end="   ")
	print(Fourth_Digit, end="   ")
	print(Fifth_Digit)




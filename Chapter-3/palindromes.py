number = int(input("Enter a number: "))

while number > 99999 or number < 10000:
	print("Invalid input!")
	number = int(input("Enter a number: "))

if number <= 99999 and number >= 10000:
	digit_1 = number // 10000
	digit_2 = (number % 10000) // 1000
	digit_3 = (number % 1000) // 100
	digit_4 = (number % 100) // 10
	digit_5 = number % 10

	new_number = str(digit_5) + str(digit_4) + str(digit_3) + str(digit_2) + str(digit_1)


if int(new_number) == number:
	print(str(number) + " is a palindrome!")
else:
	print(str(number) + " is not a palindrome!")


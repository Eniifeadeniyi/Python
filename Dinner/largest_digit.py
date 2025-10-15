number = "123"

largest_digit = number[0]
for digit in number:
	if digit > largest_digit:
		largest_digit = digit
print(largest_digit)
number = "123"

smallest_digit = number[0]
for digit in number:
	if digit < smallest_digit:
		smallest_digit = digit
print(smallest_digit)
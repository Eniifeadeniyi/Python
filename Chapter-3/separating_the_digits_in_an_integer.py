number = int(input("Enter a five-digit number: "))
digit_1 = number // 10000
digit_2 = (number % 10000) // 1000
digit_3 = (number % 1000) // 100
digit_4 = (number % 100) // 10
digit_5 = number % 10
if number in range(10000, 100000):	
	print(digit_1, digit_2, digit_3, digit_4, digit_5, end=' ')
else :
	print("Invalid input!")


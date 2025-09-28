print('Enter two integers, and I will tell you',
 'the relationships they satisfy.')


number_1 = int(input('Enter first integer: '))
number_2 = int(input('Enter second integer: '))

if number_1 == number_2:
	print(number_1, 'is equal to', number_2)
else:
	print(number_1, 'is not equal to', number_2)

if number_1 < number_2:
	 print(number_1, 'is less than', number_2)
else:
	print(number_1, 'is greater than', number_2)


if number_1 <= number_2:
	 print(number_1, 'is less than or equal to', number_2)
else:
	print(number_1, 'is greater than or equal to', number_2)

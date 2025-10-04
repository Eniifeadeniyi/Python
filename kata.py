def isEven(number):
	if number % 2 == 0:
		return True
	if number % 2 != 0:
		return False

def isPrimeNumber(number):
	divisor = 1
	factorCount = 0
	while divisor <= number :
		divide = number % divisor
		if divide == 0:
			factorCount += 1
		divisor += 1
	if factorCount == 2:
		return True
	if factorCount > 2:
		return False

def subtract(first_number, second_number):
	answer = second_number - first_number
	if first_number > second_number:
		answer = answer * -1
	return answer


def divide(first_number, second_number):
	if second_number == 0:
		return 0
	if second_number != 0:
		return first_number / second_number

def factorOf(number):
	divisor = 1
	countFactors = 0
	while divisor <= number :
		answer = number % divisor
		if answer == 0:
			countFactors += 1
		divisor += 1
	return countFactors

def isSquare(number):
	divisor = 1
	factorCount = 0
	while divisor <= number :
		divide = number % divisor
		if divide == 0 :
			factorCount += 1;
		divisor += 1;
	

	if factorCount % 2 != 0 :
		return True
	return False

def isPalindrome(number):
	if number <= 99999 and number >= 10000:
		digit_1 = number // 10000
		digit_2 = (number % 10000) // 1000
		digit_3 = (number % 1000) // 100
		digit_4 = (number % 100) // 10
		digit_5 = number % 10

	new_number = str(digit_5) + str(digit_4) + str(digit_3) + str(digit_2) + str(digit_1)


	if int(new_number) == number:
		return True
	return False

def factorialOf(number):
	factorial = 1
	counter = 1
	while counter <= number :
		factorial *= counter
		counter += 1
	return factorial


def squareOf(number):
	return number ** 2


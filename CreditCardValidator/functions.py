def check_card_type(card_number):
    if card_number.isdigit():
        if card_number[0] == "4":
            return "Visa Card"
        elif card_number[0] == "5":
            return "MasterCard"
        elif card_number[0] == "3":
            if card_number[1] == "7":
                return "American Express Card"
            else:
                return "Unknown"
        elif card_number[0] == "6":
            return "Discover Card"
        else:
            return "Unknown"
    else:
        return "Invalid input"


def double_every_second_digit(card_number):
	sum = 0
	if card_number.isdigit() and check_card_type(card_number) != "Unknown":
		for count in range(len(card_number) - 2, -1, -2):
			multiple = int(card_number[count]) * 2
			if multiple < 10:
				sum += multiple
			if multiple >= 10:
				digitSum = (multiple // 10) + (multiple % 10)
				sum += digitSum
		return sum
	else:
		return "Invalid input!"

def double_other_digits(card_number):
	sum = 0
	if card_number.isdigit() and check_card_type(card_number) != "Unknown":
		for count in range(len(card_number) - 1, -1, -2):
			sum += int(card_number[count])
		return sum
	else:
		return "Invalid input!"

def sum_both_sums(card_number):
	if double_other_digits(card_number) != "Invalid input!" and double_every_second_digit(card_number) != "Invalid input!":
		sumA = double_every_second_digit(card_number)
		sumB = double_other_digits(card_number)
		total = sumA + sumB
		return total
	else:
		return "Invalid input!"

def check_validity_of_both_sums(card_number):
	if sum_both_sums(card_number) != "Invalid input!":
		if sum_both_sums(card_number) % 10 == 0:
			return "Valid"
		else:
			return "Invalid"
	else:
		return "Invalid input!"
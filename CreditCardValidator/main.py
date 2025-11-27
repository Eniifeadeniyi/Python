from functions import *

card_number = input("Hello, kindly enter card details to verify: ")

while not card_number.isdigit():
	print("Invalid input!")
	card_number = input("Hello, kindly enter card details to verify: ")

if len(card_number) > 12 and len(card_number) < 17:
	print("Credit Card Type: " + check_card_type(card_number))
	print("Credit Card Number: " + card_number)
	print("Credit Card Digit Length: " + str(len(card_number)))
	if check_card_type(card_number) != "Unknown" and check_card_type(card_number) != "Invalid input":
		print("Credit Card Validity Status: " + check_validity_of_both_sums(card_number))
	else:
		print("Credit Card Validity Status: Invalid")
else:
	print("Credit Card Number: " + card_number)
	print("Credit Card Digit Length: " + str(len(card_number)))
	print("Credit Card Validity Status: Invalid")
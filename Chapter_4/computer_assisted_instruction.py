import random

def get_question(first_number,second_number):
	return first_number, second_number

print(get_question(first_number = random.randrange(0,11),second_number = random.randrange(0,11)))

user_input = int(input("How much is" + first_number + "times" + second_number + "?" ))
import random

def get_question():
	first_number = random.randrange(0,11)
	second_number = random.randrange(0,11)
	answer = first_number * second_number
	print (first_number, second_number)
	
	user_input = int(input("How much is " + str(first_number) + " times " + str(second_number) + "?" ))
	if user_input == answer:
		print("Very good!")
get_question()

#user_input = int(input("How much is" + first_number + "times" + second_number + "?" ))
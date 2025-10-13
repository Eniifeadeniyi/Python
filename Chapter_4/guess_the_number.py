import random

choice = "yes"

while choice == "yes":
	answer = random.randrange(1,1001)
	
	user_guess = int(input("Guess a number between 1 and 1000 included: "))

	while user_guess != answer:
		if user_guess > answer :
			print("Too high. Try again.")

		if user_guess < answer :
			print("Too low. Try again.")

		user_guess = int(input("Guess a number between 1 and 1000 included: "))

	if user_guess == answer:
		print("Congratulations. You guessed the number!")
		choice = input("Would you like to play again?: ").lower()

	if choice == "no":
		print("Goodbye!")
		break
	
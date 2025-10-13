import random

choice = "yes"
count = 0

while choice == "yes":
	count = 0
	answer = random.randrange(1,1001)
	
	user_guess = int(input("Guess a number between 1 and 1000 included: "))

	
	while user_guess != answer:
		if user_guess > answer :
			print("Too high. Try again.")
			count += 1

		if user_guess < answer :
			print("Too low. Try again.")
			count += 1

		user_guess = int(input("Guess a number between 1 and 1000 included: "))
	
	if count < 10:
		print("Either you know the secret or you got lucky!")

	if count > 10:
		print("You should be able to do better!")
	

	if user_guess == answer:
		print("Congratulations. You guessed the number!")
		choice = input("Would you like to play again?: ").lower()

	if choice == "no":
		print("Goodbye!")
		break
	
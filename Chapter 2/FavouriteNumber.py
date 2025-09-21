favourite_number = 7
#Make favourite number to be 7.

guess = int(input("Guess a number: "))
#Ask for input from user.

if guess == favourite_number:
	print("That's my favourite number!")

else:
	print("Nice try, guess again!")
#Compare user's input with set favourite number.
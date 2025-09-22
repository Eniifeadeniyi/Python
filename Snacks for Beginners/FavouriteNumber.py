#Make favourite number to be 7.
#Ask for input from user.
#Compare user's input with set favourite number.

favourite_number = 7

guess = int(input("Guess a number: "))

if guess == favourite_number:
	print("That's my favourite number!")

else:
	print("Nice try, guess again!")

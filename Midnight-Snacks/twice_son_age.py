#Declare a variable, future.
#Declare a variable, past.
#Declare a variable, father, and set it to 1.
#Declare a variable, son, and set it to 1.
#Ask user to input current age in years.
#If these conditions are met : 
	#The father's age should range from 1 to 80, and should always be greater than the son's, assign the entered value to father.
	#Ask user to input son's current age in years, and assign it to son.
#If the conditions aren't met, display Unsupported age!
#Calculate the number of years it will take for the father's age to be twice his son's, and assign it to future.
#Calculate the number of years ago the father's age was twice his son's, and assign it to past.
#Print future
#Print absolute value of past.

father = int(input("Enter your current age(in years): "))

if father > 80 or father < 1:
	print("Unsupported age!")

if father >= 1 and father <= 80:
	son = int(input("Enter your son's current age(in years): "))

if father >= 1 and father <= 80:
	future = father - (2 * son)
	print("It will take " + str(future) + " years for the father's age to be twice his son's age")
	past = abs((2 * son) - father)
	print("The father's age was twice his son's age " + str(past) + " years ago.")

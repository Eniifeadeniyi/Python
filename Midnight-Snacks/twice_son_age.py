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

from functions import *

for count in range(1,501):
	deliveries = input("Enter number of packages successfully delivered by the driver: ")

	if deliveries.isdigit():
		print(get_wage(int(deliveries)))
	else:
		print(get_wage(deliveries))

	choice = input("Do you have another delivery to record?(yes/no): ").lower()
	if choice == "no":
		print("Thanks for using the app, Bye!") 
		break


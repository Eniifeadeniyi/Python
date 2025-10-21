from functions import *

deliveries = int(input("Enter number of packages successfully delivered by the driver: "))
if deliveries >= 0 and deliveries <= 100:
	print("The driver earned: N" + str(get_wage(deliveries)))
print(get_wage(deliveries))
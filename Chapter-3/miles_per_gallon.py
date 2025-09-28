miles = 0
total_miles = 0
gallons = 0
total_gallons = 0

while miles != -1:
	total_miles += miles
	miles = int(input("Enter number of miles driven(or -1 to end): "))
	total_gallons += gallons
	gallons = int (input("Enter gallons of gasoline used: "))

average = total_miles / total_gallons
print("The overall average miles/gallon was " + str(average))
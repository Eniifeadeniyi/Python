miles = 0
total_miles = 0
gallons = 0
total_gallons = 0

while miles != -1:
	miles = int(input("Enter number of miles driven(or -1 to end): "))
	if miles == -1 :
		break
	total_miles += miles
	gallons = int (input("Enter gallons of gasoline used: "))
	journey_average = miles / gallons
	print("The miles per gallon for this journey was ", journey_average)
	total_gallons += gallons

average = total_miles / total_gallons

print("The overall average miles/gallon was " + str(average))

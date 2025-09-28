principal = 10000
rate = 0.07
year = -1

for year in range(0,31):
	interest = principal * (1 + rate) ** year
	print("After year "  + str(year) + ", amount of money is $ " + str(interest))
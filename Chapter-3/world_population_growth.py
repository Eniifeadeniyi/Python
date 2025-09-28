print("Year", "            Population", "                 Increase")
population = 8231613070
growth = 0.0085
twice = population * 2
quadruple = population * 4

for year in range(1,101):
	new_population = population * (1 + growth) ** year
	increase = new_population - population
	print(f' {year} {new_population:>25,.0f} {increase:>25,.0f}' )

for year in range(1,101):
	new_population = population * (1 + growth) ** year
	if  new_population >= twice:
		twice_year = year
		print("By year " + str(twice_year) + " the population will be, " + str(twice) + ", which is twice the current population")
		break

for year in range(1,101):
	new_population = population * (1 + growth) ** year
	if new_population >= quadruple:
		quadruple_year = year
		print("By year " + str(quadruple_year) + " the population will be, " + str(quadruple) + ", which is quadruple the current population")
		break


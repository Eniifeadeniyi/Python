#Declare a variable, number and initialize it to 0.
#Display the header: number square cube
#As long as number in within the range of 0 to 5, the square and cube of the numbers should be calculated.
#Display the number, square, and cube under each respective header title; they should be right-aligned.


number = 0
print("number", "square", "cube")
	
for number in range(6):
	square = number ** 2
	cube = number ** 3
	print(f'{number:>6} {square:>6} {cube:>4}')

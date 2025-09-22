x = 42
y = 12
z = 55

maximum = x

if y > maximum:
	maximum = y

if z > maximum:
	maximum = z


if y < maximum:
	if y > z:
		second_maximum = y 

if x < maximum:
	if x > y:
		second_maximum = x

if z < maximum:
	if z > x:
		second_maximum = z


print("The second largest number is: " + str(second_maximum))
count = 1
sum = 0

while count <= 10:
	score = int(input("Enter a student's score: "))
	sum += score
	count += 1
print("The sum of the scores is: " + str(sum))
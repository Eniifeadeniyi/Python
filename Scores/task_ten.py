count = 0
sum = 0

while count < 10:
	score = int(input("Enter a student's score: "))
	if score > 100 or score < 0:
		print("Invalid input!")
	if score >= 0 and score <= 100:
		count += 1
		sum += score
average = sum / count

print("The average of the valid scores is: " + str(average))

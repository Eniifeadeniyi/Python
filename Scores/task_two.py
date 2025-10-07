count = 0
sum = 0

while count < 10:
	score = int(input("Enter a student's score: "))
	sum += score
	count += 1
average = sum / count
print("The average of the scores is: " + str(average))
count = 0
sum = 0

while count < 10:
	score = int(input("Enter a student's score: "))
	if count % 2 == 0 :
		sum += score
	count += 1
print("The sum of the scores in even positions is: " + str(sum))

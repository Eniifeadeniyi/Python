count = 0
sum = 0
evenCounter = 0

while count < 10:
	score = int(input("Enter a student's score: "))
	if score % 2 == 0 :
		sum += score
		evenCounter += 1
	count += 1
average = sum / evenCounter 
print("The average of the even scores is: " + str(average))

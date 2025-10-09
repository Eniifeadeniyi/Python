count = 0
sum = 0.0

while(count < 10):
	score = int(input("Enter student's score: "))
	if score < 0 or score > 100:
		print("Invalid score!")
	if score >= 0 and score <= 100: 
		sum += score
	count += 1
		
average = sum / count	
print("The average of the valid scores is: " + str(average))

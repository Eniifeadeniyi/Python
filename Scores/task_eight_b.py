count = 0
sum = 0

while(count < 10):
	score = int(input("Enter student's score: "))
	if score >= 0 and score <= 100: 
		count += 1
		sum += score
	if score < 0 or score > 100:
		print("Invalid score!")
print("The sum of the valid scores is: " + str(sum))

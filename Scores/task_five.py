count = 0
sum = 0

while count < 10:
	score = int(input("Enter a student's score: "))
	if score % 2 == 0 :
		sum += score
	count += 1
print("The sum of the even scores is: " + str(sum))

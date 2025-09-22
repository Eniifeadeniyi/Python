first_score = int(input("Enter first score: "))
second_score = int(input("Enter second score:"))
third_score = int(input("Enter third score: "))

maximum = first_score

if second_score > maximum:
	maximum = second_score

if third_score > maximum:
	maximum = third_score

print("The highest score is: " + str(maximum))

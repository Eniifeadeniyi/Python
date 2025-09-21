grade = int(input("Enter your grade: "))   #Ask user to input score
#convert to integer so it returns as integer instead of string and it can be compare with 90

if grade >= 90:                            #Compare user's grade with 90
	print("Congratulations! Your grade of " + str(grade) + " earns you an A in this course.")
#convert grade back to string so it can concatenate with string.

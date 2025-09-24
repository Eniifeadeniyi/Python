# Declare a variable, first_student.
# Declare a variable, second_student.
# Declare a variable, third_student.
# Ask user to type in first student's score, and assign the input to first_student.
# Ask user to type in second student's score, and assign the input to second_student.
# Ask user to type in third student's score, and assign the input to third_student.
# Declare a variable, average.
# Assign the value of the average of the three scores to average.
# Check if average is within the range of 90 to 100, if it is, print:The class average grade is an A.
# Check if average is within the range of 80 to 89, if it is, print:The class average grade is an B.
# Check if average is within the range of 70 to 79, if it is, print:The class average grade is an C.
# Check if average is within the range of 60 to 69, if it is, print:The class average grade is an D.
# Check if average is within the range of 0 to 59, if it is, print:The class average grade is an F.



first_student = int(input("Enter first student's score: "))
second_student = int(input("Enter second student's score: "))
third_student = int(input("Enter third student's score: "))

average = (first_student + second_student + third_student) / 3

if average >= 90 and average <= 100 :
	print("The class average grade is an A")

elif average >= 80 and average < 90 :
	print("The class average grade is a B")

elif average >= 70 and average < 80 :
	print("The class average grade is a C")

elif average >= 60 and average < 70 :
	print("The class average grade is a D")

else :	
	print("The class average grade is an F")

from functions import *

menu = """
1. Add user
2. Put name for user
3. Put age for user
4. Add courses for user
5. Put address for user
6. Show user's record
7. Show user's courses
8. Show user's Zip code
9. Show user's city
10. Remove course from user's courses
11. Show usernames
12. Show number of users added
13. exit
"""

choice = ""
while(choice != "13"):
	print(menu)
	choice = input("Enter operation: ")
	match choice:
		case "13": 
			print("Bye!")
		case "1" : 
			student_id = input("Enter a unique name for username: ")
			print(make_student_personal_record(student_id))

		case "2" :
			if count_usernames() != "No user added yet!":
				student_id = input("Enter user's student_id: ")
				student_name = input("Enter name for " + student_id + ": ")
				print(put_student_name_in_record(student_id,student_name))
			else:
				print("Add a user first!")

		case "3" :
			if count_usernames() != "No user added yet!":
				student_id = input("Enter user's student_id: ")
				student_age = input("Enter age for " + student_id + ": ")
				print(put_student_age_in_record(student_id,student_age))
			else:
				print("Add a user first!")

		case "4" :
			if count_usernames() != "No user added yet!":
				display_available_courses()
				student_id = input("Enter user's student_id: ")
				student_course = input("Enter course for " + student_id + ": ")
				print(put_student_course_in_record(student_id,student_course))
			else:
				print("Add a user first!")

		case "5" :
			if count_usernames() != "No user added yet!":
				display_available_courses()
				student_id = input("Enter user's student_id: ")
				student_course = input("Enter course for " + student_id + ": ")
				print(put_student_course_in_record(student_id,student_course))
			else:
				print("Add a user first!")
	


	
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
				student_id = input("Enter user's student_id: ")
				student_city = input("Enter address city for " + student_id + ": ")
				student_zip_code = input("Enter address zip code for " + student_id + ": ")
				print(put_student_city_in_record(student_id,student_city))
				print(put_student_Zip_code_in_record(student_id,student_zip_code))
			else:
				print("Add a user first!")

		case "6" :
			if count_usernames() != "No user added yet!":
				student_id = input("Enter user's student_id: ")
				student_record = display_unique_record(student_id)
				if type(student_record) == dict:
					for key,value in student_record.items():
						print(f"{key} : {value}")
				else:
					print(student_record)
			else:
				print("Add a user first!")

		case "7" :
			if count_usernames() != "No user added yet!":
				student_id = input("Enter user's student_id: ")
				student_courses = display_unique_courses(student_id)
				if type(student_courses) == set:
					for course in student_courses:
						print(f"{course},", sep = ",", end = " ")
				else:
					print(student_courses)
			else:
				print("Add a user first!")

		case "8" :
			if count_usernames() != "No user added yet!":
				student_id = input("Enter user's student_id: ")
				print(display_unique_zip_code(student_id))
			else:
				print("Add a user first!")


		case "9" :
			if count_usernames() != "No user added yet!":
				student_id = input("Enter user's student_id: ")
				print(display_unique_city(student_id))
			else:
				print("Add a user first!")


		case "10" :
			if count_usernames() != "No user added yet!":
				display_available_courses()
				student_id = input("Enter user's student_id: ")
				student_course = input("Enter course to be removed for " + student_id + ": ")
				print(remove_from_unique_course(student_id,student_course))
			else:
				print("Add a user first!")

		case "11" :
			print(view_usernames())

		case "12" :
			print(count_usernames())
		
		case _: 
			print("Invalid input!")


	


	
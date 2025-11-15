courses_offered = {"Math", "Physics", "Computer Science", "Biology", "Chemistry", "Statistics", "English", "Economics", "History", "Philosophy", "Sociology", "Political Science", "Geography", "Psychology", "Art", "Music", "Engineering", "Law", "Medicine", "Business"}

record = {}
used_usernames = set()

def make_student_personal_record(student_id):
	if student_id.lower() not in used_usernames:
		record[student_id] = {"name" : "", "age" : "", "courses" : set(), "address" : {"city" : "", "Zip code" : ""}}
		used_usernames.add(student_id.lower())
		print(student_id + " successfully added to record!")
	else:
		print("Username already in use!")
	return record

def convert_courses_offered(courses_offered):	
	return courses_offered.lower()

compare_courses = set(map(convert_courses_offered, courses_offered))

def put_student_name_in_record(student_id,student_name):
	user = record.get(student_id, "User doesn't exist!")
	if user != "User doesn't exist!":
		user["name"] = student_name
		print(student_id + "'s" + " name successfully added!")
	else:
		print(user)
	return record


def put_student_age_in_record(student_id,student_age):
	user = record.get(student_id, "User doesn't exist!")
	if user != "User doesn't exist!":
		if student_age.isdigit():
			user["age"] = int(student_age)
		print(student_id + "'s" + " age successfully added!")
	else:
		print(user)
	return record


def put_student_course_in_record(student_id,student_course):
	user = record.get(student_id, "User doesn't exist!")
	if user != "User doesn't exist!":
		if student_course.lower() in compare_courses:
			user["courses"].add(unique_course)
			print(student_id + "'s course successfully added!")
		else:
			print("Course not offered in this department!")
	else:	
		print(user)
	return record


def put_student_city_in_record(student_id,student_city):
	user = record.get(student_id, "User doesn't exist!")
	if user != "User doesn't exist!":
		if not student_city.isdigit():
			user["city"] = student_city
			print(student_id + "'s city successfully added!")
		else:
			print("Invalid input!")
	else:
		print(user)
	return record


def put_student_Zip_code_in_record(student_id, student_zip_code):
	user = record.get(student_id, "User doesn't exist!")
	if user != "User doesn't exist!":
		if  student_zip_code.isdigit() and len(student_zip_code) == 6:
			user["Zip code"] = student_zip_code
			print(student_id + "'s zip code successfully added!")
		else:
			print("Invalid input!")
	else:
		print(user)
	return record

def display_unique_record(student_id):
	user = record.get(student_id, "Username doesn't exist!")
	if user != "Username doesn't exist!":
		if len(user) != 0:
			return user
		else:
			return "No record added yet for " + student_id
	else:
		return user
	

def display_unique_courses(student_id):
	user = record.get(student_id, "Username doesn't exist!")
	if user != "Username doesn't exist!":
		if len(user["courses"]) != 0:
			return user["courses"]
		else:
			return "No courses added yet for " + student_id
	else:
		return user

def display_unique_zip_code(student_id):
	user = record.get(student_id, "Username doesn't exist!")
	if user != "Username doesn't exist!":
		home = user["address"]
		if len(home) != 0:
			if len(home["Zip code"]) != 0:
				return home["Zip code"]
			else:
				return "No Zip code added yet for " + student_id
		else:
			return "No address added yet for " + student_id
	else:
		return user
	
def display_unique_city(student_id):
	user = record.get(student_id, "Username doesn't exist!")
	if user != "Username doesn't exist!":
		home = user["address"]
		if len(home) != 0:
			if len(home["city"]) != 0:
				return home["city"]
			else:
				return "No city added yet for " + student_id
		else:
			return "No address added yet for " + student_id
	else:
		return user

def add_to_unique_course(student_id,added_course):
	user = record.get(student_id, "Username doesn't exist!")
	if user != "Username doesn't exist!":
		course = user["courses"]
		if added_course not in course and added_course in courses_offered:
			course.add(added_course)
			return "Course successfully added for " + student_id
		elif added_course in course:
			return "Course already offered by " + student_id

		elif added_course not in courses_offered:
			return "Course not offered in this department!"
	else:
		return user

def remove_from_unique_course(student_id,removed_course):
	user = record.get(student_id, "Username doesn't exist!")
	if user != "Username doesn't exist!":
		course = user["courses"]
		if removed_course in course:
			course.remove(removed_course)
			return "Course successfully removed for " + student_id
		elif removed_course not in course:
			return "Course not offered by " + student_id

	else:
		return user

def view_usernames():
	if len(record) != 0:
		for key in record:
			print(f"{key}", end = " ")
	else:
		return "No user added yet!"
	return ""

def count_usernames():
	count = 0
	if len(record) != 0:
		for key in record:
			count += 1
		return count
	else :
		return "No user added yet!"



		
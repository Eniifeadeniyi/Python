courses_offered = {"Math", "Physics", "Computer Science", "Biology", "Chemistry", "Statistics", "English", "Economics", "History", "Philosophy", "Sociology", "Political Science", "Geography", "Psychology", "Art", "Music", "Engineering", "Law", "Medicine", "Business"}

record = {}
record1 = {}

def make_student_personal_record(student_id):
	if student_id.lower() not in list(record1.keys()):
		record1[student_id.lower()] = {}
		record[student_id] = {}
	else:
		print("Username already in use!")
	return record

def convert_courses_offered(courses_offered):	
	return courses_offered.lower()

compare_courses = set(map(convert_courses_offered, courses_offered))

def make_student_courses_list(student_course):
	unique_course = []
	if not student_course.isdigit():
		if student_course.lower() in compare_courses:
			unique_course.append(student_course)
		else:
			print("Course not offered in this department!")
	else:
		print("Invalid input!")
	return set(unique_course)

def make_student_address(student_city, student_zip_code):
	unique_address = {}
	if not student_city.isdigit() and student_zip_code.isdigit() and len(student_zip_code) == 6:
		unique_address["city"] = student_city
		unique_address["Zip code"] = student_zip_code
	else:
		print("Invalid input!")
	return unique_address

def collect_student_details(student_name, student_age, unique_course, unique_address):
	unique_record = {}
	if not student_name.isdigit() and student_age.isdigit():
		unique_record["name"] = student_name
		unique_record["age"] = int(student_age)
		unique_record["courses"] = unique_course
		unique_record["address"] = unique_address
	else:
		print("Invalid input!")
	return unique_record

def update_record(record,unique_record,student_id):
	record[student_id] = unique_record
	return record

def display_unique_record(record,student_id):
	user = record.get(student_id, "Username doesn't exist!")
	if user != "Username doesn't exist!":
		if len(user) != 0:
			return user
		else:
			return "No record added yet for " + student_id
	else:
		return user
	

def display_unique_courses(record,student_id):
	user = record.get(student_id, "Username doesn't exist!")
	if user != "Username doesn't exist!":
		if len(user["courses"]) != 0:
			return user["courses"]
		else:
			return "No courses added yet for " + student_id
	else:
		return user

def display_unique_zip_code(record,student_id):
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
	
def display_unique_city(record,student_id):
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

def add_to_unique_course(record,student_id,added_course):
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

def remove_from_unique_course(record,student_id,removed_course):
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

def view_usernames(record):
	if len(record) != 0:
		for key in record:
			print(f"{key}", end = " ")
	else:
		return "No user added yet!"
	return ""

def count_usernames(record):
	count = 0
	if len(record) != 0:
		for key in record:
			count += 1
		return count
	else :
		return "No user added yet!"



		
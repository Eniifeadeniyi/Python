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
			print("Course not offered!")
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

def display_record(student_id):
	return record.get(student_id, "Username doesn't exist!")

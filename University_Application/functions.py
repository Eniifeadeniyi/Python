courses_offered = ["Math", "Physics", "Computer Science", "Biology", "Chemistry", "Statistics", "English", "Economics", "History", "Philosophy", "Sociology", "Political Science", "Geography", "Psychology", "Art", "Music", "Engineering", "Law", "Medicine", "Business"]

record = {}
used_usernames = set()

def make_student_personal_record(student_id):
	if student_id.lower() not in used_usernames:
		record[student_id] = {"name" : "", "age" : "", "courses" : set(), "address" : {"city" : "", "Zip code" : ""}}
		used_usernames.add(student_id.lower())
		return(student_id + " successfully added to record!")
	else:
		return("Username already in use!")
	

def convert_courses_offered(courses_offered):	
	return courses_offered.lower()

compare_courses = set(map(convert_courses_offered, courses_offered))

def put_student_name_in_record(student_id,student_name):
	user = record.get(student_id, "Username doesn't exist!")
	if user != "Username doesn't exist!":
		user["name"] = student_name
		return(student_id + "'s" + " name successfully added!")
	else:
		return(user)
	


def put_student_age_in_record(student_id,student_age):
	user = record.get(student_id, "Username doesn't exist!")
	if user != "Username doesn't exist!":
		if student_age.isdigit():
			user["age"] = int(student_age)
		return(student_id + "'s" + " age successfully added!")	
	else:
		return(user)
	
def display_available_courses():
	print("Available courses: ", end = " ")
	print(courses_offered)

def put_student_course_in_record(student_id,student_course):
	user = record.get(student_id, "Username doesn't exist!")
	if user != "Username doesn't exist!":
		if student_course.lower() in compare_courses and student_course not in user["courses"]:
			user["courses"].add(student_course)
			return(student_id + "'s course successfully added!")		
		elif student_course in user["courses"]:
			return "Course already offered by " + student_id

		elif student_course.lower() not in compare_courses:
			return("Course not offered in this department!")
	else:	
		return(user)
	
def put_student_city_in_record(student_id,student_city):
	user = record.get(student_id, "Username doesn't exist!")
	if user != "Username doesn't exist!":
		if not student_city.isdigit():
			user["city"] = student_city
			return(student_id + "'s city successfully added!")
		else:
			return("City must contain letters!")
	else:
		return(user)

def put_student_Zip_code_in_record(student_id, student_zip_code):
	user = record.get(student_id, "Username doesn't exist!")
	if user != "Username doesn't exist!":
		if  student_zip_code.isdigit() and len(student_zip_code) == 6:
			user["Zip code"] = int(student_zip_code)
			return(student_id + "'s zip code successfully added!")
		else:
			return("Zip code must be 6 digits!")
	else:
		return(user)

def count(user):
	count = 0
	if user["name"] != "":
		count += 1
	if user["age"] != "":
		count += 1
	if user["courses"] != set():
		count += 1
	house = user["address"]
	if house["city"] != "" or house["Zip code"] != "":
		count += 1
	return count

def display_unique_record(student_id):
	user = record.get(student_id, "Username doesn't exist!")
	if user != "Username doesn't exist!":
		if count(user) != 0:
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
		house = user["address"]
		if house["Zip code"] != "":
			return house["Zip code"]
		else:
			return "No Zip code added yet for " + student_id
	else:
		return user
	
def display_unique_city(student_id):
	user = record.get(student_id, "Username doesn't exist!")
	if user != "Username doesn't exist!":
		house = user["address"]
		if house["city"] != "":
			return house["city"]
		else:
			return "No city added yet for " + student_id
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
	if len(used_usernames) != 0:
		return used_usernames
	else:
		return "No user added yet!"

def count_usernames():
	if len(record) != 0:
		return len(record)
	else :
		return "No user added yet!"





		
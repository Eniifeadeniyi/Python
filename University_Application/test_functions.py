import unittest
from functions import *

class TestUniversityApplicationFunctions(unittest.TestCase):
	
	def test_that_make_student_personal_record_works(self):
		actual = make_student_personal_record("Enidgr8")
		expected = {"Enidgr8" : {}}
		self.assertEqual(actual,expected)

	def test_that_make_student_courses_set_function_works(self):
		actual = make_student_courses_list("Math")
		expected = {"Math"}
		self.assertEqual(actual,expected)

	def test_that_make_student_courses_set_doesnt_add_unoffered_course(self):
		actual = make_student_courses_list("Speaker")
		expected = set()
		self.assertEqual(actual,expected)

	def test_that_make_student_address_works(self):
		actual = make_student_address("Lagos","115021")
		expected = {"city" : "Lagos", "Zip code" : "115021",}
		self.assertEqual(actual,expected)

	def test_that_make_student_address_only_takes_valid_input(self):
		actual = make_student_address("Lagos","11502")
		expected = {}
		self.assertEqual(actual,expected)
		actual = make_student_address("Lagos1","11502a")
		expected = {}
		self.assertEqual(actual,expected)

	def test_that_collect_student_details_works(self):
		actual = collect_student_details("Eniife", "17", {"Math", "Physics", "Biology"}, {"city" : "Lagos", "Zip code" : "115021"})
		expected = {"name" : "Eniife", "age" : 17, "courses" : {"Math", "Physics", "Biology"}, "address" : {"city" : "Lagos", "Zip code" : "115021"}}
		self.assertEqual(actual,expected)

	def test_that_update_record_works(self):
		record = {}
		actual = update_record(record,{"name" : "Eniife", "age" : 17, "courses" : {"Math", "Physics", "Biology"}, "address" : {"city" : "Lagos", "Zip code" : "115021"}}, "eni")
		expected = {"eni" : {"name" : "Eniife", "age" : 17, "courses" : {"Math", "Physics", "Biology"}, "address" : {"city" : "Lagos", "Zip code" : "115021"}},}
		self.assertEqual(actual,expected)

	def test_that_display_record_works(self):
		record = {"tolu" : {"name" : "Tolu", "age" : 17, "courses" : {"Math", "Physics", "Biology"}, "address" : {"city" : "Lagos", "Zip code" : "115021"}}, }
		actual = display_unique_record(record,"Enii")
		expected = "Username doesn't exist!"
		self.assertEqual(actual,expected)

	def test_that_you_cant_display_record_of_unknown_username(self):
		record = {"eni" : {"name" : "Eniife", "age" : 17, "courses" : {"Math", "Physics", "Biology"}, "address" : {"city" : "Lagos", "Zip code" : "115021"}},}
		actual = display_unique_record(record,"eni")
		expected = {"name" : "Eniife", "age" : 17, "courses" : {"Math", "Physics", "Biology"}, "address" : {"city" : "Lagos", "Zip code" : "115021"}}
		self.assertEqual(actual,expected)


	def test_that_display_unique_courses_works(self):
		record = {"eni" : {"name" : "Eniife", "age" : 17, "courses" : {"Math", "Physics", "Biology"}, "address" : {"city" : "Lagos", "Zip code" : "115021"}},}
		actual = display_unique_courses(record,"eni")
		expected = {"Math", "Physics", "Biology"}
		self.assertEqual(actual,expected)

	def test_that_you_cant_display_course_of_unknown_username(self):
		record = {"tolu" : {"name" : "Tolu", "age" : 17, "courses" : {"Math", "Physics", "Biology"}, "address" : {"city" : "Lagos", "Zip code" : "115021"}}, }
		actual = display_unique_courses(record,"eni")
		expected = "Username doesn't exist!"
		self.assertEqual(actual,expected)

	def test_that_display_unique_zip_code_works(self):
		record = {"eni" : {"name" : "Eniife", "age" : 17, "courses" : {"Math", "Physics", "Biology"}, "address" : {"city" : "Lagos", "Zip code" : "115021"}},}
		actual = display_unique_zip_code(record,"eni")
		expected = "115021"
		self.assertEqual(actual,expected)

	def test_that_display_unique_zip_code_does_not_take_in_unknown_username(self):
		record = {"eni" : {"name" : "Eniife", "age" : 17, "courses" : {"Math", "Physics", "Biology"}, "address" : {"city" : "Lagos", "Zip code" : "115021"}},}
		actual = display_unique_zip_code(record,"enii")
		expected = "Username doesn't exist!"
		self.assertEqual(actual,expected)

	def test_that_display_unique_city_works(self):
		record = {"eni" : {"name" : "Eniife", "age" : 17, "courses" : {"Math", "Physics", "Biology"}, "address" : {"city" : "Lagos", "Zip code" : "115021"}},}
		actual = display_unique_city(record,"eni")
		expected = "Lagos"
		self.assertEqual(actual,expected)

	def test_that_display_unique_city_does_not_take_in_unknown_username(self):
		record = {"eni" : {"name" : "Eniife", "age" : 17, "courses" : {"Math", "Physics", "Biology"}, "address" : {"city" : "Lagos", "Zip code" : "115021"}},}
		actual = display_unique_city(record,"enii")
		expected = "Username doesn't exist!"
		self.assertEqual(actual,expected)

	def test_that_add_to_unique_course_works(self):
		record = {"eni" : {"name" : "Eniife", "age" : 17, "courses" : {"Math", "Physics", "Biology"}, "address" : {"city" : "Lagos", "Zip code" : "115021"}},}
		actual = add_to_unique_course(record,"eni","Chemistry")
		expected = "Course successfully added for eni"
		self.assertEqual(actual,expected)

	def test_that_you_cant_add_course_to_unknown_username_record(self):
		record = {"eni" : {"name" : "Eniife", "age" : 17, "courses" : {"Math", "Physics", "Biology"}, "address" : {"city" : "Lagos", "Zip code" : "115021"}},}
		actual = add_to_unique_course(record,"enii","Chemistry")
		expected = "Username doesn't exist!"
		self.assertEqual(actual,expected)

	def test_that_you_can_only_add_courses_available(self):
		record = {"eni" : {"name" : "Eniife", "age" : 17, "courses" : {"Math", "Physics", "Biology"}, "address" : {"city" : "Lagos", "Zip code" : "115021"}},}
		actual = add_to_unique_course(record,"eni","Ballet")
		expected = "Course not offered in this department!"
		self.assertEqual(actual,expected)

	def test_that_course_is_not_added_if_already_offered(self):
		record = {"eni" : {"name" : "Eniife", "age" : 17, "courses" : {"Math", "Physics", "Biology"}, "address" : {"city" : "Lagos", "Zip code" : "115021"}},}
		actual = add_to_unique_course(record,"eni","Math")
		expected = "Course already offered by eni"
		self.assertEqual(actual,expected)


	def test_that_remove_from_unique_course_works(self):
		record = {"eni" : {"name" : "Eniife", "age" : 17, "courses" : {"Math", "Physics", "Biology"}, "address" : {"city" : "Lagos", "Zip code" : "115021"}},}
		actual = remove_from_unique_course(record,"eni","Biology")
		expected  = "Course successfully removed for eni"
		self.assertEqual(actual,expected)

	def test_that_remove_from_unique_course_doesnt_remove_unoffered_course(self):
		record = {"eni" : {"name" : "Eniife", "age" : 17, "courses" : {"Math", "Physics", "Biology"}, "address" : {"city" : "Lagos", "Zip code" : "115021"}},}
		actual = remove_from_unique_course(record,"eni","Chemistry")
		expected  = "Course not offered by eni"
		self.assertEqual(actual,expected)

	def test_that_remove_from_unique_course_doesnt_remove_course_for_unknown_username(self):
		record = {"eni" : {"name" : "Eniife", "age" : 17, "courses" : {"Math", "Physics", "Biology"}, "address" : {"city" : "Lagos", "Zip code" : "115021"}},}
		actual = remove_from_unique_course(record,"enii","Chemistry")
		expected  = "Username doesn't exist!"
		self.assertEqual(actual,expected)

	def test_that_view_usernames_works(self):
		record = {"eni" : {"name" : "Eniife", "age" : 17, "courses" : {"Math", "Physics", "Biology"}, "address" : {"city" : "Lagos", "Zip code" : "115021"}}, "tolu" : {"name" : "Tolu", "age" : 17, "courses" : {"Math", "Physics", "Biology"}, "address" : {"city" : "Lagos", "Zip code" : "115021"}},}
		actual = view_usernames(record)
		self.assertEqual(actual,"")

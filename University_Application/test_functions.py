import unittest
from functions import *

class TestUniversityApplicationFunctions(unittest.TestCase):
	
	def test_that_make_student_personal_record_works(self):
		record = {}
		actual = make_student_personal_record("Enidgr8")
		expected = {"Enidgr8" : {}}
		self.assertEqual(actual,expected)

	def test_that_make_student_courses_list_function_works(self):
		actual = make_student_courses_list("Math")
		expected = {"Math"}
		self.assertEqual(actual,expected)
		actual = make_student_courses_list("Speaker")
		expected = set()
		self.assertEqual(actual,expected)

	def test_that_make_student_address_works(self):
		actual = make_student_address("Lagos","115021")
		expected = {"city" : "Lagos", "Zip code" : "115021",}
		self.assertEqual(actual,expected)
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
		actual = display_record("Enii")
		expected = "Username doesn't exist!"
		self.assertEqual(actual,expected)
		actual = display_record()
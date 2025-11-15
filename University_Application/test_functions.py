import unittest
from functions import *

class TestUniversityApplicationFunctions(unittest.TestCase):
	
	def test_that_make_student_personal_record_works(self):
		actual = make_student_personal_record("Eni")
		expected = {"Eni" : {"name" : "", "age" : "", "courses" : set(), "address" : {"city" : "", "Zip code" : ""}},}
		self.assertEqual(actual,expected)

	def test_that_put_student_name_in_record_works(self):
		actual = put_student_name_in_record("Eni","Eniife")
		expected = {"Eni" : {"name" : "Eniife", "age" : "", "courses" : set(), "address" : {"city" : "", "Zip code" : ""}},}
		self.assertEqual(actual,expected)

	def test_that_put_student_name_in_record_doesnt_take_unknown_username(self):
		actual = put_student_name_in_record("Enii","tobi")
		expected = {"Eni" : {"name" : "Eniife", "age" : "", "courses" : set(), "address" : {"city" : "", "Zip code" : ""}},}
		self.assertEqual(actual,expected)

	def test_that_put_student_age_in_record_works(self):
		actual = put_student_age_in_record("Eni","17")
		expected = {"Eni" : {"name" : "Eniife", "age" : 17, "courses" : set(), "address" : {"city" : "", "Zip code" : ""}},}
		self.assertEqual(actual,expected)

	def test_that_put_student_age_in_record_doesnt_take_unknown_username(self):
		actual = put_student_age_in_record("Enii","17")
		expected = {"Eni" : {"name" : "", "age" : "", "courses" : set(), "address" : {"city" : "", "Zip code" : ""}},}
		self.assertEqual(actual,expected)

	

import unittest
from functions import *

class TestUniversityApplicationFunctions(unittest.TestCase):

	def test_that_make_student_personal_record_works(self):
		actual = make_student_personal_record("Eni")
		expected = "Eni successfully added to record!"
		self.assertEqual(actual,expected)
		actual = make_student_personal_record("Eni")
		expected = "Username already in use!"
		self.assertEqual(actual,expected)

	def test_that_put_student_name_in_record_works(self):
		actual = put_student_name_in_record("Eni","Eniife")
		expected = "Eni's name successfully added!"
		self.assertEqual(actual,expected)

	def test_that_put_student_name_in_record_doesnt_take_unknown_username(self):
		actual = put_student_name_in_record("Enii","tobi")
		expected = "Username doesn't exist!"
		self.assertEqual(actual,expected)


	def test_that_put_student_age_in_record_works(self):
		actual = put_student_age_in_record("Eni","17")
		expected = "Eni's age successfully added!"
		self.assertEqual(actual,expected)

	def test_that_put_student_age_in_record_doesnt_take_unknown_username(self):
		actual = put_student_age_in_record("Enii","19")
		expected = "Username doesn't exist!"
		self.assertEqual(actual,expected)


	def test_that_put_student_course_in_record_works(self):
		actual = put_student_course_in_record("Eni","Math")
		expected = "Eni's course successfully added!"
		self.assertEqual(actual,expected)

	def test_that_put_student_course_in_record_doesnt_take_unknown_username(self):
		actual = put_student_course_in_record("Enii","Math")
		expected = "Username doesn't exist!"
		self.assertEqual(actual,expected)

	def test_that_put_student_course_in_record_doesnt_take_unavailable_course(self):
		actual = put_student_course_in_record("Eni", "Ballet")
		expected = "Course not offered in this department!"
		self.assertEqual(actual,expected)

	def test_that_put_student_city_in_record_works(self):
		actual = put_student_city_in_record("Eni","Lagos")
		expected = "Eni's city successfully added!"
		self.assertEqual(actual,expected)

	def test_that_put_student_city_in_record_doesnt_take_unknown_username(self):
		actual = put_student_city_in_record("Enii","Lagos")
		expected = "Username doesn't exist!"
		self.assertEqual(actual,expected)

	def test_that_put_student_city_in_record_doesnt_take_invalid_input(self):
		actual = put_student_city_in_record("Eni", "123456")
		expected = "City must contain letters!"
		self.assertEqual(actual,expected)

	def test_that_put_student_Zip_code_in_record_works(self):
		actual = put_student_Zip_code_in_record("Eni","115021")
		expected = "Eni's zip code successfully added!"
		self.assertEqual(actual,expected)

	def test_that_put_student_Zip_code_in_record_doesnt_take_unknown_username(self):
		actual = put_student_Zip_code_in_record("Enii","115021")
		expected = "Username doesn't exist!"
		self.assertEqual(actual,expected)

	def test_that_put_student_Zip_code_in_record_only_takes_int(self):
		actual = put_student_Zip_code_in_record("Eni", "12345l")
		expected = "Zip code must be 6 digits!"
		self.assertEqual(actual,expected)

		

	




	

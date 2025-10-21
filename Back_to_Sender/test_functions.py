import unittest
from functions import *

class TestForDispatchRiderApp(unittest.TestCase):
	def test_that_get_wage_works(self):
		expected = 8200
		actual = get_wage(20)
		self.assertEqual(actual,expected)

	def test_that_get_wage_doesnt_take_in_negative_input(self):
		expected = "Invalid input!"
		actual = get_wage(-2)
		self.assertEqual(actual,expected)

	def test_that_get_wage_doesnt_take_in_string_input(self):
		expected = "Invalid input!"
		actual = get_wage(";")
		self.assertEqual(actual,expected)

	def test_that_get_wage_doesnt_take_in_input_greater_than_hundred(self):
		expected = "Invalid input!"
		actual = get_wage(120)
		self.assertEqual(actual,expected)
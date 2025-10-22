import unittest
from functions import *

class TestForDispatchRiderApp(unittest.TestCase):
	def test_that_get_wage_works(self):
		expected = "The driver earned: N5000"
		actual = get_wage(0)
		self.assertEqual(actual,expected)
		expected = "The driver earned: N8200"
		actual = get_wage(20)
		self.assertEqual(actual,expected)
		expected = "The driver earned: N15000"
		actual = get_wage(50)
		self.assertEqual(actual,expected)
		expected = "The driver earned: N21250"
		actual = get_wage(65)
		self.assertEqual(actual,expected)
		expected = "The driver earned: N42000"
		actual = get_wage(74)
		self.assertEqual(actual,expected)
		expected = "The driver earned: N55000"
		actual = get_wage(100)
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
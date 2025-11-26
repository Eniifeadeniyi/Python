import unittest
from functions import *

class TestFunctions(unittest.TestCase):
	def test_that_check_card_type_works(self):
		actual = check_card_type("3788576018402626")
		expected = "American Express Card"
		self.assertEqual(actual, expected)
		
	def test_that_double_every_second_digit_works(self):
		actual = double_every_second_digit("4388576018402626")
		expected = 37
		self.assertEqual(actual,expected)

	def test_that_double_other_digits_works(self):
		actual = double_other_digits("4388576018402626")
		expected = 38
		self.assertEqual(actual,expected)
	
	def test_that_sum_both_sums_works(self):
		actual = sum_both_sums("4388576018402626")
		expected = 75
		self.assertEqual(actual,expected)

	def test_that_check_validity_of_both_sums_works(self):
		actual = check_validity_of_both_sums("4388576018402626")
		expected = "Invalid"
		self.assertEqual(actual,expected)
		actual = check_validity_of_both_sums("4388576018410707")
		expected = "Valid"
		self.assertEqual(actual,expected)
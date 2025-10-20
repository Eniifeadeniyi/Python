import unittest
from functions import *

class TestForFuelDispenserSystemFunctions(unittest.TestCase):
	def test_that_petrol_amount_function_works(self): 
		actual = petrol_amount(2000)
		expected = f"""
			Product : Petrol       								
			Amount : #2000.00 								
			Liters : 2.00L   						
			Thanks for patronizing Eniife's Station 			
				Hope to see you again!			
		
			"""
		self.assertEqual(actual,expected)

	def test_that_petrol_amount_function_doesnt_take_string_input(self):
		actual = petrol_amount("tgr")
		expected = "Invalid input!"
		self.assertEqual(actual,expected)

	def test_that_petrol_amount_function_doesnt_take_amount_less_than_a_liter(self):
		actual = petrol_amount(500)
		expected = "Amount must be above a liter price!!!"
		self.assertEqual(actual,expected)

	def test_that_petrol_liter_function_works(self): 
		actual = petrol_liter(2)
		expected = f"""
			Product : Petrol       								
			Amount : #2000.00 								
			Liters : 2.00L   						
			Thanks for patronizing Eniife's Station 			
				Hope to see you again!			
		
			"""
		self.assertEqual(actual,expected)

	def test_that_petrol_liter_function_doesnt_take_string_input(self):
		actual = petrol_liter("tgr")
		expected = "Invalid input!"
		self.assertEqual(actual,expected)

	def test_that_petrol_liter_function_only_takes_liter_between_one_and_fifty(self):
		actual = petrol_liter(-1)
		expected = "Liters must be between 1-50!!!"
		self.assertEqual(actual,expected)


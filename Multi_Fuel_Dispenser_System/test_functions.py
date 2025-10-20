import unittest
from functions import *

class TestForFuelDispenserSystemFunctions(unittest.TestCase):
	def test_that_petrol_amount_function_works(self): 
		actual = petrol_amount(2000)
		expected = 2000, 2
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
		expected = 2000,2
		self.assertEqual(actual,expected)

	def test_that_petrol_liter_function_doesnt_take_string_input(self):
		actual = petrol_liter("tgr")
		expected = "Invalid input!"
		self.assertEqual(actual,expected)

	def test_that_petrol_liter_function_only_takes_liter_between_one_and_fifty(self):
		actual = petrol_liter(-1)
		expected = "Liters must be between 1-50!!!"
		self.assertEqual(actual,expected)


	def test_that_diesel_amount_function_works(self): 
		actual = diesel_amount(3000)
		expected = 3000,2
		self.assertEqual(actual,expected)

	def test_that_diesel_amount_function_doesnt_take_string_input(self):
		actual = diesel_amount("tgr")
		expected = "Invalid input!"
		self.assertEqual(actual,expected)

	def test_that_diesel_amount_function_doesnt_take_amount_less_than_a_liter(self):
		actual = diesel_amount(500)
		expected = "Amount must be above a liter price!!!"
		self.assertEqual(actual,expected)

	def test_that_diesel_liter_function_works(self): 
		actual = diesel_liter(2)
		expected = 3000,2
		self.assertEqual(actual,expected)

	def test_that_diesel_liter_function_doesnt_take_string_input(self):
		actual = diesel_liter("tgr")
		expected = "Invalid input!"
		self.assertEqual(actual,expected)

	def test_that_diesel_liter_function_only_takes_liter_between_one_and_fifty(self):
		actual = diesel_liter(-1)
		expected = "Liters must be between 1-50!!!"
		self.assertEqual(actual,expected)



	def test_that_kerosene_amount_function_works(self): 
		actual = kerosene_amount(2400)
		expected = 2400,2
		self.assertEqual(actual,expected)

	def test_that_kerosene_amount_function_doesnt_take_string_input(self):
		actual = kerosene_amount("tgr")
		expected = "Invalid input!"
		self.assertEqual(actual,expected)

	def test_that_kerosene_amount_function_doesnt_take_amount_less_than_a_liter(self):
		actual = kerosene_amount(500)
		expected = "Amount must be above a liter price!!!"
		self.assertEqual(actual,expected)

	def test_that_kerosene_liter_function_works(self): 
		actual = kerosene_liter(2)
		expected = 2400,2
		self.assertEqual(actual,expected)

	def test_that_kerosene_liter_function_doesnt_take_string_input(self):
		actual = kerosene_liter("tgr")
		expected = "Invalid input!"
		self.assertEqual(actual,expected)

	def test_that_kerosene_liter_function_only_takes_liter_between_one_and_fifty(self):
		actual = kerosene_liter(-1)
		expected = "Liters must be between 1-50!!!"
		self.assertEqual(actual,expected)


	def test_that_gas_amount_function_works(self): 
		actual = gas_amount(3600)
		expected = 3600,2
		self.assertEqual(actual,expected)

	def test_that_gas_amount_function_doesnt_take_string_input(self):
		actual = gas_amount("tgr")
		expected = "Invalid input!"
		self.assertEqual(actual,expected)

	def test_that_gas_amount_function_doesnt_take_amount_less_than_a_liter(self):
		actual = gas_amount(500)
		expected = "Amount must be above a liter price!!!"
		self.assertEqual(actual,expected)

	def test_that_gas_liter_function_works(self): 
		actual = gas_liter(2)
		expected = 3600,2
		self.assertEqual(actual,expected)

	def test_that_gas_liter_function_doesnt_take_string_input(self):
		actual = gas_liter("tgr")
		expected = "Invalid input!"
		self.assertEqual(actual,expected)

	def test_that_gas_liter_function_only_takes_liter_between_one_and_fifty(self):
		actual = gas_liter(-1)
		expected = "Liters must be between 1-50!!!"
		self.assertEqual(actual,expected)






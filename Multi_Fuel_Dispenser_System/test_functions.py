import unittest
from functions import *

class TestForFuelDispenserSystemFunctions(unittest.TestCase):
	def test_that_petrol_amount_function_exists(self):
		receipt = f"""
		=========================================================
		=	Product : Petrol       				=
		=	Amount : #2000.00  				=
		=	Liters : 2.00L		   			=
		=	Thanks for patronizing Eniife's Station 	=
		=		Hope to see you again!			=
		=========================================================
		"""
		actual = petrol_amount(2000)
		expected = receipt		
		self.assertEqual(actual,expected)
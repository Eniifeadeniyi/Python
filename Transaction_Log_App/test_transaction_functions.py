import unittest
from transaction_functions import *
transactions = []
class TransactionLogFunctions(unittest.TestCase):
	def test_that_deposit_function_exists(self):
		deposit(100)


	def test_that_deposit_increases_balance(self):
		actual = deposit(100)
		expected = 100,transactions
		self.assertEqual(actual,expected)
		actual = deposit(500)
		expected = 500,transactions
		self.assertEqual(actual,expected)

	
	def test_that_deposit_takes_in_float(self):
		actual = deposit(100.50)
		expected = 100.50,transactions
		self.assertEqual(actual,expected)
	

	def test_that_deposit_doesnt_take_negative_numbers(self):
		actual = deposit(-200)
		expected = 0,transactions
		self.assertEqual(actual,expected)
		

	def test_that_deposit_doesnt_take_in_string(self):
		actual = deposit(";")
		expected = 0,transactions
		self.assertEqual(actual,expected)
		

	def test_that_withdraw_function_exists(self):
		withdraw(100)
		

	def test_that_withdraw_function_updates_balance(self):
		actual = withdraw(500, balance = 1000)
		expected = 500,transactions
		self.assertEqual(actual,expected)
		

	def test_that_withdraw_cannot_be_greater_than_balance(self):
		actual = withdraw(500)
		expected = 0,transactions
		self.assertEqual(actual,expected)
		
	
	def test_that_withdraw_cannot_take_in_string(self):
		actual = withdraw("vring")
		expected = 0,transactions
		self.assertEqual(actual,expected)
		

	def test_that_history_works(self):
		actual = history(transactions)
		expected = transanctions
		self.assertEqual(actual,expected)
		

	

	
		
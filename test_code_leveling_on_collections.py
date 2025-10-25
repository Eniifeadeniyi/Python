import unittest
from code_leveling_on_collections import *

class TestCodeLevelingOnCollections(unittest.TestCase):
	def test_that_add_to_tuple_works(self):
		actual = add_to_tuple((1,2,3,4,5),6,10,15)
		expected = (1,2,3,4,5,6,10,15)
		self.assertEqual(actual,expected)

	def test_that_edit_tuple_works(self):
		actual = edit_tuple(1,2,[3,4],5)
		expected = [1,2,[3,99],5]
		self.assertEqual(actual,expected)

	def test_that_unpack_works(self):
		actual = unpack(10,20,30,40)
		expected = 10,20,(30,40)
	
	

	
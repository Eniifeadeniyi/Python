import unittest
from functions import *

class TestBookSuggestionSystemFunctions (unittest.TestCase):
	def test_that_get_random_book_works(self):
		books = ["lion","Chukwuebuka and the Tortoise", "Femi who Cried Wolf", "Eniife is cool"]
		get_random_book(books)

	def test_that_get_random_page_works(self):
		get_random_page()

	def test_that_get_random_page_is_not_the_same_sequentially(self):
		books = ["lion","Chukwuebuka and the Tortoise", "Femi who Cried Wolf", "Eniife is cool"]
		first_random = get_random_page()
		second_random = get_random_page()
		self.assertNotEqual(first_random,second_random)
		
	def test_that_get_random_book_is_not_the_same_sequentially(self):
		books = ["lion","Chukwuebuka and the Tortoise", "Femi who Cried Wolf", "Eniife is cool"]
		first_random = get_random_book(books)
		second_random = get_random_book(books)
		self.assertNotEqual(first_random,second_random)


	def test_that_add_book_updates_book_list(self):
		books = ["lion","Chukwuebuka and the Tortoise", "Femi who Cried Wolf", "Eniife is cool"]
		actual = add_book("Romeo and Juliet", books)
		expected = ["lion","Chukwuebuka and the Tortoise", "Femi who Cried Wolf", "Eniife is cool", "Romeo and Juliet"]
		self.assertEqual(actual,expected)

	def test_that_book_doesnt_update_if_the_book_already_exists(self):
		books = ["lion","Chukwuebuka and the Tortoise", "Femi who Cried Wolf", "Eniife is cool"]
		actual = add_book("Lion", books)
		expected = books
		self.assertEqual(actual,expected)

	def test_that_remove_book_works(self):
		books = ["lion","Chukwuebuka and the Tortoise", "Femi who Cried Wolf", "Eniife is cool"]
		actual = remove_book("lion",books)
		expected = ["Chukwuebuka and the Tortoise", "Femi who Cried Wolf", "Eniife is cool"]
		self.assertEqual(actual,expected)

	def test_that_remove_book_doesnt_remove_book_that_is_not_in_the_list(self):
		books = ["lion","Chukwuebuka and the Tortoise", "Femi who Cried Wolf", "Eniife is cool"]
		actual = remove_book("eniife",books)
		expected = books
		self.assertEqual(actual,expected)

	def test_that_show_books_works(self):
		books = ["lion","Chukwuebuka and the Tortoise", "Femi who Cried Wolf", "Eniife is cool"]
		expected = books
		actual = show_books(books)
		self.assertEqual(actual,expected)

				
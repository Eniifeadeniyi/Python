import random
books = ["The Tortoise and The Hare", "Ralia the Sugar Girl", "Half of a Yellow Sun", "Daughters who Walked This Path", "The Boy in the Striped Pyjamas", "Things Fall Apart", "Americanah", "Children of Blood and Bone", "The Thing Around Your Neck", "Gifted Hands", "Think Big"]


def get_random_book(books):
	return random.choice(books)

def get_random_page():
	return random.randrange(1,101)

def get_suggestions(books):
	book_suggest = get_random_book(books)
	page_suggest = get_random_page()
	return book_suggest, page_suggest

def convert_book_title(title):
	return title.lower()
converted = list(map(convert_book_title, books))

def add_book(book,converted):
	if book.lower() not in converted:
		books.append(book)
		print("Book succesfully added!")
	if book.lower() in converted:
		print("Book already exists!")
	return books


def remove_book(book,converted):
	if book.lower() in converted:
		books.remove(book)
		print("Book successfully removed!")
	else:
		print("Book not found!")

	return books 

def show_books(books):
	return books
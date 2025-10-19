from functions import *

books = ["The Tortoise and The Hare", "Ralia the Sugar Girl", "Half of a Yellow Sun", "Daughters who Walked This Path", "The Boy in the Striped Pyjamas", "Things Fall Apart", "Americanah", "Children of Blood and Bone", "The Thing Around Your Neck", "Gifted Hands", "Think Big"]

print("Welcome to the Book Suggestion System!")

while True:
	menu = """
		1. Get Suggestions
		2. Add Book
		3. Remove Book
		4. Update book
		5. Show all books
		 
	"""
	print(menu)
	operation = input("Enter operation: ")
	match operation:
		case "1" : 
			choice = ""
			while choice != "no":
				book, page = get_suggestions(books)
				print(book)
				print(page)
				choice = input("Would you like to get another suggestion?(yes/no): ").lower()
		
		case "2" :
			book = input("Enter the book title: ")
			add_book(book,converted)

		case "3" :
			print(books)
			remove = input("Enter the book title: ")
			remove_book(remove,converted)

		case "4" :
			wrong = input("Enter the old title: ")
			correct = input("Enter the new title: ")
			update_book(wrong,correct,books)
		
		case "5" :
			print(show_books(books))

		case _: print("Please enter a number from below!")
								
					
				
	
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

words = ["python", "programming", "data", "science", "learning", "challenge", "function", "variable", "loop", "string","is","fun"]

people = [
    {"name": "Alice", "age": 25, "city": "Lagos"},
    {"name": "Ben", "age": 30, "city": "Abuja"},
    {"name": "Clara", "age": 22, "city": "Port Harcourt"},
    {"name": "David", "age": 27, "city": "Enugu"},
    {"name": "Ella", "age": 35, "city": "Ibadan"},
    {"name": "Frank", "age": 29, "city": "Kano"},
    {"name": "Grace", "age": 24, "city": "Abeokuta"},
    {"name": "Henry", "age": 31, "city": "Jos"},
    {"name": "Ivy", "age": 28, "city": "Asaba"},
    {"name": "James", "age": 33, "city": "Uyo"}
]

sentences = ["Eniife is so cool", "Martins is a donkey", "Nissi is smart", "Dotun has an app"]

#Beginner:
#1
def get_square(numbers):
	return numbers ** 2
print(list(map(get_square,numbers)))


#2
def get_even_numbers(numbers):
	return numbers % 2 == 0
print(list(filter(get_even_numbers,numbers)))


#3
def get_odd_numbers(numbers):
	return numbers % 2 != 0
odd = list(filter(get_odd_numbers,numbers))
def get_cube(odd):
	return odd ** 3
print(list(map(get_cube,odd)))


#4
def get_sum(numbers,next_number):
	return numbers + next_number
print(reduce(get_sum,numbers))


#5
def get_max(numbers,next_number):
	max = numbers
	if next_number > max:
		max = next_number
	return max
print(reduce(get_max,numbers))



#Intermediate:
#6
def get_length(words):
	return len(words)
print(list(map(get_length,words)))

#7
def get_some_words(words):
	return len(words) < 4
print(list(filter(get_some_words,words)))

#8
def join_words(words,next_word):
	return words + " " + next_word
print(reduce(join_words,words))

#9
def select(people):
	return people["age"] > 30
print(list(filter(select,people)))

#10
def get_names(people):
	return people["name"]
print(list(map(get_names,people)))


#Advanced:
#11
def get_even(numbers):
	return numbers % 2 == 0
even = list(filter(get_even,numbers))
def get_even_squares(even):
	return even ** 2
squares = list(map(get_even_squares,even))
def get_sum(squares,next_number):
	return squares + next_number
print(reduce(get_sum,squares))


#12
def split(sentences):
	return sentence

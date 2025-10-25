numbers = [1,2,3,4,5,6]
fruits = ["apple", "banana", "cherry", "kiwi", "grapes"]
words = ["I", "love", "Eniife's", "drawings."]
#1
def get_square(numbers):
	return numbers ** 2
print(list(map(get_square, numbers)))

#2
def get_length(words):
	return len(words)
print(list(map(get_length,fruits)))

#3
def get_even(numbers):
	return numbers % 2 == 0
print(list(filter(get_even, numbers)))

#4
def remove_greater_than_five(words):
	return len(words) <= 5
print(list(filter(remove_greater_than_five,fruits)))

#5
from functools import reduce
def join_words(words,next_word):
	return words + "-" + next_word
print(reduce(join_words,words))

#1
def convert_to_number(strings):
	return int(strings)
strings = ["1", "2", "3"]
print(list(map(convert_to_number, strings)))

#2
def add_ten(numbers):
	return numbers + 10
numbers = [0,5,10,15]
print(list(map(add_ten,numbers)))

#3
def convert_temperature(temperatures):
	return f'{(temperatures * 1.8) + 32 : .2f}'
temperatures = [0,20,37,100]
print(list(map(convert_temperature,temperatures)))

#4
def remove_values(values):	
	return type(values) == int
values = [1,None,3,None,5]
print(list(filter(remove_values,values)))

#5
def get_multiples_of_three(numbers):
	return numbers % 3 == 0
numbers = [1,3,4,6,9,12]
print(list(filter(get_multiples_of_three,numbers)))

#6
def get_positive_numbers(numbers):
	return numbers >= 0
numbers = [-2,-1,0,1,2]
print(list(filter(get_positive_numbers,numbers)))

#7
def get_age_greater_than_twenty_five(data):
	return data["age"] > 25
data = [{"name" : "Alice", "age" : 30}, {"name" : "Bob", "age" : 20}]
print(list(filter(get_age_greater_than_twenty_five,data)))

#8
from functools import reduce
def get_sum(numbers,next_number):
	return numbers + next_number
numbers = [1,2,3,4,5]
print(reduce(get_sum,numbers))

#9
def get_product(numbers,next_number):
	return numbers * next_number
numbers = [2,3,4]
print(reduce(get_product,numbers))

#10
def get_maximum(numbers,next_number):
	max = numbers
	if next_number > max:
		max = next_number
	return max
numbers = [3,7,2,9,1]
print(reduce(get_maximum,numbers))

#11
def join_words(words,next_word):
	return words + next_word
words = ["Hello", " ", "World"]
print(reduce(join_words,words))

#13
def square(numbers):
	return numbers ** 2 
numbers = [1,2,3]
square = list(map(square,numbers))
def sum_square(square,next_square):
	return square + next_square
print(reduce(sum_square,square))

#12
def merge_dictionaries(dictionaries,next_dictionary):
	return dictionaries | next_dictionary
dictionaries = [{"a": 1}, {"b" : 2}, {"c" : 3}]
print(reduce(merge_dictionaries,dictionaries))
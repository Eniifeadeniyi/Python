from functools import reduce

#1
def add_to_tuple(tuple,*increase):
	tuple +=  increase
	return tuple


#2
def edit_tuple(*numbers):
	numbers = list(numbers)
	numbers[2][1] = 99
	return numbers


#4
def unpack(*numbers):
	a, b, *c = numbers
	print(a,b,c)

#5
def add(input):
	for count in range(len(input)):
		input[count] = sum(input[count])
	return input
		
input = [[2,3,4],[1,5,7],[4,6,8]]
print(add(input))

#7
def get_even(numbers):
	return numbers % 2 == 0
numbers = (number for number in range(1,22))
print(list(filter(get_even,numbers)))

#8
def get_some_strings(words):
	return len(words) > 5
words = ["cat", "elephant", "tiger", "lion"]
print(list(filter(get_some_strings,words)))


#10
def get_multiples_of_three_and_five(numbers):
	return numbers % 15 == 0 
numbers = [number for number in range(1,52)]
print(list(filter(get_multiples_of_three_and_five,numbers)))

#11
def get_palindromes(words):
	return words == words[-1::-1]
words = ["level", "world", "madam", "python"]
print(list(filter(get_palindromes,words)))

#12
def convert(strings):
	return strings.upper()
strings = ["python", "java", "c++"]
print(list(map(convert,strings)))

#13
def get_square(numbers):
	return numbers ** 2
numbers = [1,2,3,4,5,6,7,8,9,10]
print(list(map(get_square,numbers)))

#14
def first_letter(names):
	return names[0].upper() + names[1:]
names = ["john", "mary", "steve"]
print(list(map(first_letter,names)))

#15
def inflate(prices):
	return prices + (0.1 * prices)
prices = [100,200,300]
print(list(map(inflate,prices)))

#16
def get_sum(numbers,next_number):
	return numbers + next_number
numbers = (number for number in range(1,51))
print(reduce(get_sum,numbers))

#17
def get_maximum(numbers,next_number):
	max = numbers
	if next_number > max:
		max = next_number
	return max
numbers = [3,5,9,2,8]
print(reduce(get_maximum,numbers))

#18
def join_strings(words,next_word):
	return words + " " + next_word
words = ["I", "love", "Python"]
print(reduce(join_strings,words))

#19
def get_squares(numbers):
	return numbers ** 2
numbers = [1,2,3,4]
squares = list(map(get_squares,numbers))
def get_product(squares,next_square):
	return squares + next_square
print(reduce(get_product,squares))


#9
#def get_some_tuples(list):
#	for row in range(list.length):
#		for column in range(list[row].length):
#			return list[row][column] > 2
#list = [(1,"A"), (4, "B"), (2, "C")] 
#print(list(filter(get_some_tuples,list)))


#21
#I DONT UNDERSTAND
#def int(nsfr):
#	pass

#20
#NOT WORKING
#def get_sum(numbers):
#	return sum(numbers)

#6
#I DONT GET THE QUESTION

#3
#NOT WORKING
#fruits = ("apple", "banana", "cherry")
#fruits_list = list(fruits)
#fruits_list.append("mango")
#print(tuple(fruits_list))



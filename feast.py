#1
def get_third_element(list):
	return list[2]


nums = [10, 20, 30, 40 , 50]
print(get_third_element(nums))


#2
def change_last_colour(list):
	list[-1] = "yellow"
	return list

colours = ["red", "green", "blue"]
print(change_last_colour(colours))

#3
def add_colour_purple(colours):
	colours.append("purple")
	return colours

print(add_colour_purple(colours))


#4
def remove_element(list):
	list.remove(3)
	return list

my_list = [1,2,3,4,5]
print(remove_element(my_list))


#5
def length_of_each_element(list):
	length_list = []
	for element in list:
		length_list.append(len(element))
	return length_list

my_list = ["Alice", "Oluwatobiloba", "Chukwuebuka"]
print(length_of_each_element(my_list))


#6
def ascending_order(list):
	list.sort()
	return list

nums = [4,1,3,9,2,11,-1]
print(ascending_order(nums))


#7
def only_even_numbers(list):
	even_list = []
	for element in list:
		if element % 2 == 0:
			even_list.append(element)
	return even_list

nums = [4,1,3,9,2]
print(only_even_numbers(nums))


#8
def combine_list(first_list, second_list):
	first_list.extend(second_list)
	return first_list


a = [1,2,3]
b = [4,5,6]
print(combine_list(a,b))



#9
def return_some_words(list):
	new_list = []
	for element in list:
		if len(element) > 3:
			new_list.append(element)
	return new_list


words = ["lamb", "kit", "yam", "kings", "dogs", "man"]
print(return_some_words(words))


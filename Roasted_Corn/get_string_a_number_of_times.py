def get_string_a_number_of_times(word,number):
	if type(number) == int:
		return word * number
	if type(number) != int:
		return word

print(get_string_a_number_of_times("paul",10))
print(get_string_a_number_of_times("paul",10.9))
def get_letters_in_odd_positions(word):
	count = 0
	new_word = " "
	for letters in word:
		if count % 2 != 0:
			new_word += letters
		count += 1
	return new_word

print(get_letters_in_odd_positions("semicolon"))	
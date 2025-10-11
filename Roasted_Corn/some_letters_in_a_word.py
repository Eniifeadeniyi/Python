def get_some_letters_in_a_word(word):
	for letters in word:
		if len(word) >= 2:
			return word[0] + word[1] + word[-2] + word[-1]
		if len(word) < 2:
			return " "
print(get_some_letters_in_a_word("o"))
def get_longest_word(*words):
	longest_word = words[0]
	for word in words:
		if len(word) > len(word[0]) :
			longest_word = word
	return longest_word, len(longest_word)

print(get_longest_word("Eniifeoluwa","Chukwuebuka","Oluwatosin","Ifeoluwatomi"))
def reverse_each_word(sentence):
	result = ""
	words = sentence.split(" ")
	for count in range(len(words)):
		word = words[count]
		reverse = word[-1::-1]
		result += reverse + " "
	return result

sentence = input("Enter a sentence: ")
print(reverse_each_word(sentence))
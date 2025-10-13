def add_ing(word):
	if len(word) >= 3:
		if word[-1] == "g" and word[-2] == "n" and word[-3] == "i": 
					return word + "ly"

		return word + "ing"

	if len(word) < 3:
		return word


print(add_ing("Eniifeoluwa"))

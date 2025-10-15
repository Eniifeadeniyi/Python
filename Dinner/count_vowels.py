word = "Eniifeoluwa"
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0
count = 0
for letter in word.lower():
	if letter == "a" :
		count_a += 1

	if letter == "e" :
		count_e += 1

	if letter == "i" :
		count_i += 1

	if letter == "o" :
		count_o += 1

	if letter == "u" :
		count_u += 1

count = count_a + count_e + count_i + count_o + count_u

print(count)
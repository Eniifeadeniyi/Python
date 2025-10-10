strings = ["book", "father", "glasses", "bottle", "book", "phone"]

count = 0

for item in strings:
	count += 1
if count >= 2:
	if strings[0] == strings[count - 1] :
		print(strings)


	
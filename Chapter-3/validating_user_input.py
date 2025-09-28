passes = 0
fails = 0

result = int(input("Enter student's grade(1=pass 2=fail) or -1 to end: "))

while result != -1:
	result = int(input("Enter student's grade(1=pass 2=fail) or -1 to end: "))

	if result == 1:
		passes += 1

	elif result == 2:
		fails += 1
	elif result != 1 and result != 2 and result != -1:
		result = int(input("Enter student's grade(1=pass 2=fail) or -1 to end: "))

	if result == -1:
		print(str(passes) + " people passed.")
		print(f'{fails} people failed.')





























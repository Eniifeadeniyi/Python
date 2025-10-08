def contains_elements(target, *numbers):
	count = 0
	for number in numbers:
		if number == target:
			count += 1
		if count > 0:
			return True
		else :
			return False
print(contains_elements(12,3,4,5))
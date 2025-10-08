def count_occurrence(target, *numbers):
	count = 0
	for number in numbers:
		if number == target:
			count += 1
	return count
print(count_occurrence(12,12,15,12,14))
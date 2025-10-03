def only_floats(a,b):
	if a >= 0.0 or b >= 0.0:
		return 1
	if a >= 0 or b >= 0:
		return 0
	if a >= 0.0 and b >= 0.0:
		return 2

print(only_floats(12.1,23))
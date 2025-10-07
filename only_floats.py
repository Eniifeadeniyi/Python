def only_floats(a,b):
	if type(a) == float and type(b) == float:
		return 2
	if type(a) == float or type(b) == float:
		return 1
	if type(a) == int and type(b) == int:
		return 0

print(only_floats(12.1,23))

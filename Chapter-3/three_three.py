"""
	This program will display > on even lines, and < on odd lines.
"""


for row in range(10):
	for column in range(10):
		print('>' if column % 2 == 1 else '<', end='')
	print()

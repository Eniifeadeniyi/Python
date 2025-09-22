"""
	Program to calculate user's maximum heart rate, and range of user's target heart rate.
"""

age = int(input("Enter your age: "))

maximum = 220 - age
target_minimum = 0.50 * maximum
target_maximum = 0.85 * maximum

print("Your maximum heart rate is:", maximum, "bpm")
print("Your target heart rate is:", target_minimum, "bpm", "-", target_maximum, "bpm")
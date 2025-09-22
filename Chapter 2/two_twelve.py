"""
	Program to calculate compound interest made on $10000 after 10, 20 , and 30 years at 7% p.a.
"""
principle = 10000
rate = 0.07

amount = principle * (1 + rate) ** 10
print("After 10 years: $", amount)

amount = principle * (1 + rate) ** 20
print("After 20 years: $", amount)

amount = principle * (1 + rate) ** 30
print("After 30 years: $", amount)



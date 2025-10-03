def amount(investment_amount, monthly_interestRate, years):
	future_investment_value = investment_amount * ((1 + monthly_interestRate) ** (years * 12))
	return future_investment_value

print(amount(1000, 0.12, 4))
import math

amount_invested = 1000
annual_rate = 0.07
num_years= 10
amount_expected = amount_invested * (math.pow((1 + annual_rate),10))
print(amount_expected)

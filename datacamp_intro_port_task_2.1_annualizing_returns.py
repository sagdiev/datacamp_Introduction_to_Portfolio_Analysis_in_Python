# Calculate total rate of return from portfolio AUM
total_return = (pf_AUM[-1] - pf_AUM[0]) / pf_AUM[0]
# print(months)
# print(pf_returns.head())
# print(pf_returns.tail())
# print(pf_AUM.head())
# print(pf_AUM.tail())

# Calculate the total return from the S&P500 value series
total_return = (sp500_value[-1] - sp500_value[0]) / sp500_value[0]
print(total_return)

# Annualize the total return spanning 4 years
annualized_return = ((1 + total_return)**(1/4))-1
print (annualized_return)


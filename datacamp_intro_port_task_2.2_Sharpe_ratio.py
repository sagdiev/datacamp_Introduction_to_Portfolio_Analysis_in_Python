# Calculate total return and annualized return from price data
total_return = (sp500_value[-1] - sp500_value[0]) / sp500_value[0]

# Annualize the total return over 4 year
annualized_return = ((1 + total_return)**(1/4))-1

# Create the returns data
returns_sp500 = sp500_value.pct_change()

# Calculate annualized volatility from the standard deviation
vol_sp500 = returns_sp500.std() * np.sqrt(250)

# Calculate the Sharpe ratio
sharpe_ratio = ((annualized_return - rfr) / vol_sp500)
print (sharpe_ratio)

# Calculate total return and annualized return from price data
total_return = (pf_AUM[-1] - pf_AUM[0]) / pf_AUM[0]

# Annualize the total return over 4 year
annualized_return = ((1 + total_return)**(12/months))-1

# Create the returns data
pf_returns = pf_AUM.pct_change()

# Calculate annualized volatility from the standard deviation
vol_pf = pf_returns.std()*np.sqrt(250)

# Calculate the Sharpe ratio
sharpe_ratio = ((annualized_return - rfr) /vol_pf)
print (sharpe_ratio)


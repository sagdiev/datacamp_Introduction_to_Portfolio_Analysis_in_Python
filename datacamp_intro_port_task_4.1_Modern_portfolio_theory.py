# Import the packages 
from pypfopt import risk_models
from pypfopt import expected_returns
from pypfopt.efficient_frontier import EfficientFrontier

# Calculate expected returns mu 
mu = expected_returns.mean_historical_return(stock_prices)

# Calculate the covariance matrix S
Sigma = risk_models.sample_cov(stock_prices)

# Obtain the efficient frontier
ef = EfficientFrontier(mu, Sigma)
print (mu, Sigma)


# Get the returns from the stock price data
returns=stock_prices.pct_change()

# Calculate the annualized covariance matrix
covMatrix = returns.cov()*252

# Calculate the covariance matrix Sigma from a`PyPortfolioOpt` function
Sigma = risk_models.sample_cov(stock_prices)

# Print both covariance matrices
print (covMatrix,Sigma)


# Get the minimum risk portfolio for a target return
weights = ef.efficient_return(0.2)
print (weights)

# Show portfolio performance
ef.portfolio_performance(verbose=True)
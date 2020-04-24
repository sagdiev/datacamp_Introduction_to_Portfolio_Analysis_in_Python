# Check the portfolio weights
print(portfolio_data.pf_weights.sum())

# Calculate return of the portfolio
total_return_pf = (portfolio_data['pf_weights']*portfolio_data['mean_return']).sum()

# Calculate return of the benchmark
total_return_bm = (portfolio_data['bm_weights']*portfolio_data['mean_return']).sum()

# Calculate and print the active return
active_return = total_return_pf - total_return_bm
print ("%.2f%%" % active_return)


# Print the sum of the bm and pf weights
print (portfolio_data.pf_weights.sum())
print (portfolio_data.bm_weights.sum())

# Print the sum of the bm and pf weights
print (portfolio_data.bm_weights.sum())
print (portfolio_data.pf_weights.sum())

# Group dataframe by GICS sectors
grouped_df=portfolio_data.groupby('GICS Sector').sum()

# Calculate active weights of portfolio
grouped_df['active_weight']=grouped_df['pf_weights']-grouped_df['bm_weights']
print (grouped_df['active_weight'])
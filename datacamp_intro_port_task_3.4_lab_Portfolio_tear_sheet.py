# Set the index to datetime
returns_sp500.index=pd.to_datetime(returns_sp500.index)

# Ensure the returns are a series
returns=returns_sp500['S&P500']
# print(returns.head())

# Create the returns tear sheet
fig = pf.create_returns_tear_sheet(returns, return_fig=True)

# Display a zoomed in version of the tear sheet
display_tear_sheet()


# Define sector mappings
sect_map = {'COST': 'Consumer Goods',
            'INTC': 'Technology',
            'CERN': 'Healthcare',
            'GPS': 'Technology',
            'MMM': 'Construction',
            'DELL': 'Technology',
            'AMD': 'Technology'}

# Create sector exposure tear sheet
pf.create_position_tear_sheet(returns, positions, sector_mappings=sect_map)
display_tear_sheet()
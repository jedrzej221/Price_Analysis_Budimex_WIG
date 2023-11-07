import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

# Define the stock symbol (ticker)
stock_symbol = "BUD"

# Define the start and end date for data collection (10 years)
start_date = "2013-11-01"
end_date = "2023-11-01"

# Fetch historical stock price data
budimex_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Calculate daily returns
budimex_data['Daily_Return'] = budimex_data['Adj Close'].pct_change()

# Calculate and visualize rolling statistics
rolling_window = 30  # You can adjust this window size as needed

budimex_data['Rolling_Mean'] = budimex_data['Adj Close'].rolling(window=rolling_window).mean()
budimex_data['Rolling_Std'] = budimex_data['Adj Close'].rolling(window=rolling_window).std()

# Calculate annualized volatility
annualized_volatility = budimex_data['Daily_Return'].std() * np.sqrt(252)

# Calculate annualized mean return
annualized_mean_return = budimex_data['Daily_Return'].mean() * 252

# Calculate the Sharpe ratio
risk_free_rate = 0.03  # You can adjust this rate according to the risk-free rate in your analysis
sharpe_ratio = (annualized_mean_return - risk_free_rate) / annualized_volatility

# Visualize the stock price and rolling statistics
plt.figure(figsize=(12, 8))
plt.title(f'{stock_symbol} Stock Prices from {start_date} to {end_date}')
plt.plot(budimex_data['Adj Close'], label='Stock Price')
plt.plot(budimex_data['Rolling_Mean'], label=f'{rolling_window}-Day Rolling Mean')
plt.plot(budimex_data['Rolling_Std'], label=f'{rolling_window}-Day Rolling Std')
plt.xlabel('Date')
plt.ylabel('Price (PLN)')
plt.legend()
plt.grid(True)
plt.show()

# Display statistics
print("Basic Statistics:")
print(budimex_data.describe())
print(f"Annualized Volatility: {annualized_volatility:.4f}")
print(f"Annualized Mean Return: {annualized_mean_return:.4f}")
print(f"Sharpe Ratio: {sharpe_ratio:.4f}")

# Visualize the daily returns
plt.figure(figsize=(12, 6))
plt.title(f'{stock_symbol} Daily Returns from {start_date} to {end_date}')
plt.plot(budimex_data['Daily_Return'])
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.grid(True)
plt.show()
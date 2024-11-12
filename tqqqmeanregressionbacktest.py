import pandas as pd
import numpy as np

# Load TQQQ data
data = pd.read_csv('/mnt/data/TQQQ (2).csv')
data['Date'] = pd.to_datetime(data['Date'])

# Backtest function definition
def backtest_tqqq(data):
    # Shift the close to get the previous day's close
    data['Previous_Close'] = data['Close'].shift(1)
    # Condition: trade if today's open is lower than the previous close
    data['Open_Less_Than_Previous_Close'] = data['Open'] < data['Previous_Close']
    # Calculate returns only for the days where the previous days experienced negative growth
    data['Daily_Return'] = data['Close'] / data['Open'] - 1  # Return for days with trades
    data['Trade_Return'] = np.where(data['Open_Less_Than_Previous_Close'], data['Daily_Return'], 0)

    # Calculate yearly returns
    data['Year'] = data['Date'].dt.year
    yearly_returns = data.groupby('Year')['Trade_Return'].apply(lambda x: (1 + x[x != 0]).prod() - 1)

    # Calculate risk-adjusted yearly return
    average_yearly_return = yearly_returns.mean()
    risk_adjusted_yearly_return = average_yearly_return / yearly_returns.std()

    # Trade outcome calculations
    trades = data['Trade_Return'][data['Trade_Return'] != 0]
    trades_won = trades[trades > 0].count()
    trades_lost = trades[trades < 0].count()
    win_rate = trades_won / len(trades) * 100 if len(trades) > 0 else 0
    avg_trade_return = trades.mean()

    # Sharpe Ratio (annualized assuming 252 trading days in a year)
    daily_sharpe_ratio = trades.mean() / trades.std() if trades.std() != 0 else 0
    sharpe_ratio = daily_sharpe_ratio * np.sqrt(252)

    # Percentage of days invested
    days_invested = (data['Trade_Return'] != 0).sum()
    pct_days_invested = days_invested / len(data) * 100

    # Print results
    print("Yearly Returns:")
    print(yearly_returns)
    print("\nRisk-Adjusted Yearly Return:", risk_adjusted_yearly_return)
    print("Average Trade Return:", avg_trade_return)
    print("Trades Won:", trades_won)
    print("Trades Lost:", trades_lost)
    print("Win Rate (%):", win_rate)
    print("Sharpe Ratio:", sharpe_ratio)
    print("Percentage of Days Invested:", pct_days_invested)

# Run the backtest and output results
backtest_tqqq(data)

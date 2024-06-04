Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> import alpaca_trade_api as tradeapi
... from datetime import datetime, timedelta
... import pytz
... 
... # Alpaca API credentials
... API_KEY = 'your_api_key'
... API_SECRET = 'your_api_secret'
... BASE_URL = 'https://paper-api.alpaca.markets'  # or use the live URL for real trading
... 
... # Initialize Alpaca API
... api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')
... 
... def get_yesterday_data():
...     # Get the date of the previous trading day
...     today = datetime.now(pytz.timezone('America/New_York')).date()
...     yesterday = today - timedelta(days=1)
...     
...     # Fetch historical data for TQQQ
...     data = api.get_barset('TQQQ', 'day', start=yesterday.isoformat(), end=today.isoformat())
...     return data['TQQQ'][0]
... 
... def trade():
...     # Get yesterday's trading data
...     yesterday_data = get_yesterday_data()
...     
...     if not yesterday_data:
...         print("No trading data available for yesterday.")
...         return
... 
...     open_price = yesterday_data.o
...     close_price = yesterday_data.c
... 
...     # Determine the trading strategy based on yesterday's growth
...     position_type = 'long' if close_price < open_price else 'short'
    
    # Get the current account information
    account = api.get_account()
    
    # Calculate the amount to invest
    investment = float(account.buying_power)
    
    # Place the order
    if position_type == 'long':
        order = api.submit_order(
            symbol='TQQQ',
            qty=investment // open_price,  # number of shares to buy
            side='buy',
            type='market',
            time_in_force='day'
        )
    else:
        order = api.submit_order(
            symbol='TQQQ',
            qty=investment // open_price,  # number of shares to short
            side='sell',
            type='market',
            time_in_force='day'
        )

    print(f"Placed a {position_type} order for TQQQ.")

if __name__ == '__main__':
    trade()

This bot trades the NYSE ticker $TQQQ. The bot utilizes a mean regression indicator to open long and short positions.

The bot’s long/short indications are as follows: If the previous trading day experienced negative growth, a long position is opened and is closed at the end of the trading day. If the previous trading day experienced positive growth, a short position is opened and is closed at the end of the trading day. There is no stop loss or take profit price action level.

The rationale for this strategy is that a positive growing asset will always follow a positive slope in the long run, so any deviations should reverse back to the average price of the asset. Thus, negative growth should indicate more than a 50% chance of the price of the asset experiencing positive growth in the same time period and vice versa. Additionally, it is hypothesized that purchasing the asset after a day of negative growth allows the asset to be bought at a “discount” and selling the asset after a day of positive growth allows the asset to be sold at a “premium”.

Disclaimer: the bot is updated to initiate short positions but the backtest is not!

100% of the portfolio is dedicated to every trade.

The original code for the bot was written in Python, using the “alpaca-trade-api” package. This was eventually translated into PineScript to work with the TradingView API. Both files can be found on the GitHub repository.

Thank you for visiting!

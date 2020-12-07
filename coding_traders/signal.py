import pandas_datareader as pdr
from datetime import datetime as dt
from datetime import timedelta
import numpy as np
import matplotlib.pyplot as plt


class SignalDetector:
    def get_stock_data(self, stock_symbol, start=None, end=None):
        """ Get the stock data of the specified symbol over a specified time frame """

        # default time frame
        if end is None:
            end = dt.now()
        if start is None:
            start = end - timedelta(days=365)

        # get stock data
        stock_data = pdr.get_data_yahoo(stock_symbol, start, end)
        return stock_data

    def plot_stock(self, stock):
        """ Plots the stock """
        stock['Close'].plot(grid=True)
        plt.show()

    def percentage_change_adj_close(self):
        daily_close = self.apple[['Adj Close']]
        daily_pct_change = daily_close.pct_change()
        daily_pct_change.fillna(0, inplace=True)

        daily_log_returns = np.log(daily_close.pct_change()+1)

    def calculate_volatility(self):
        """ Calculate the volatility of the given stock """
        min_periods = 75
        volume = self.daily_pct_change.rolling(min_periods).std() * np.sqrt(min_periods)

        volume.plot(figsize=(10, 8))
        plt.show()

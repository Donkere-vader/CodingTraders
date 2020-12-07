import pandas_datareader as pdr
import datetime
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelmin, argrelmax


class SignalDetector:
    def stock_data(self, stock_symbol):
        start = datetime.datetime(2019, 12, 4)
        end = datetime.datetime(2020, 12, 4)
        apple = pdr.get_data_yahoo(stock_symbol, start, end)
        return apple

    # print(apple.describe())

    # print(apple.tail())

    def plot_stock(self):
        prices = self.apple['Close']
        self.apple['Close'].plot(grid=True)

        plt.show()

    def percentage_change_adj_close(self):
        daily_close = self.apple[['Adj Close']]
        daily_pct_change = daily_close.pct_change()
        daily_pct_change.fillna(0, inplace=True)

        print(daily_pct_change)

        daily_log_returns = np.log(daily_close.pct_change()+1)

        print(daily_log_returns)

    def calculate_volatility(self):
        # Calculate the volatility of the given stock
        min_periods = 75
        volume = self.daily_pct_change.rolling(min_periods).std() * np.sqrt(min_periods)

        volume.plot(figsize=(10, 8))

        plt.show()


class CodingTraders:
    def __init__(self):
        signaldetector = SignalDetector()
        stockinformation_apple = signaldetector.stock_data("AAPL")
        all_highs = stockinformation_apple['High']
        all_lows = stockinformation_apple['Low']
        r = 1.05
        n = len(stockinformation_apple['High'])
        min_and_max_values = []
        print(len(all_highs))
        print(len(all_lows))
        self.main_program_loop(all_highs, all_lows, r, n, min_and_max_values)

    def main_program_loop(self, all_highs, all_lows, r, n, min_and_max_values):
        def find_first():
            imin = 1
            imax = 1
            i = 2
            while i < n and all_lows[i] / all_lows[imin] < r and all_highs[imax] / all_highs[i] < r:
                if all_lows[i] < all_lows[imin]:
                    imin = i
                if all_highs[i] > all_highs[imax]:
                    imax = i
                i = i + 1

            if imin < imax:
                print(all_lows[imin])
                print(imin)
                min_and_max_values.append(all_lows[imin])
            else:
                print(all_highs[imax])
                print(imax)
                min_and_max_values.append(all_highs[imax])

            return i

        def find_minimum(i):
            imin = i

            while i < n and all_lows[i]/all_lows[imin] < r:
                if all_lows[i] < all_lows[imin]:
                    imin = i
                i = i+1
            if i < n and all_lows[imin] < all_lows[i]:
                print(all_lows[imin])
                print(imin)
                min_and_max_values.append(all_lows[imin])

            return i

        def find_maximum(i):
            imax = i

            while i < (n-1) and all_highs[imax]/all_highs[i] < r:
                if all_highs[i] > all_highs[imax]:
                    imax = i
                i = i + 1

            if i < n and all_highs[imax] > all_highs[i]:
                print(all_highs[imax])
                print(imax)
                min_and_max_values.append(all_highs[imax])

            return i

        i = find_first()

        if i < n and all_highs[i] > all_lows[1]:
            i = find_maximum(i)

        while i < n:
            i = find_minimum(i)
            i = find_maximum(i)

        print(min_and_max_values)

        for i in range(len(min_and_max_values)-3):
            if min_and_max_values[i] > min_and_max_values[i + 2] and min_and_max_values[i + 1] < \
                    min_and_max_values[i + 3]:
                print("----------------------------")
                print(min_and_max_values[i])
                print(min_and_max_values[i + 1])
                print(min_and_max_values[i + 2])
                print(min_and_max_values[i + 3])
            elif min_and_max_values[i] < min_and_max_values[i + 2] and min_and_max_values[i + 1] > \
                    min_and_max_values[i + 3]:
                print("----------------------------")
                print(min_and_max_values[i])
                print(min_and_max_values[i + 1])
                print(min_and_max_values[i + 2])
                print(min_and_max_values[i + 3])


CodingTraders()

# Different approach to find important minima and maxima of the high
not_in_use = """N = 1  # number of iterations
highs = apple['High'].dropna().copy()  # make a series of Highs
lows = apple['Low'].dropna().copy()  # make a series of Lows
for i in range(N):
    highs = highs.iloc[argrelmax(highs.values)[0]]  # locate maxima in Highs
    lows = lows.iloc[argrelmin(lows.values)[0]]  # locate minima in Lows
    highs = highs[~highs.index.isin(lows.index)]  # drop index that appear in both
    lows = lows[~lows.index.isin(highs.index)]  # drop index that appear in both

print(highs)
highs.plot(grid=True)
plt.show()

print("---------------------------------")

print(lows)
lows.plot(grid=True)
plt.show()"""


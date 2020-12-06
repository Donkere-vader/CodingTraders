import pandas_datareader as pdr
import datetime
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelmin, argrelmax


# Imports all available stock information on Yahoo! Finance.
start = datetime.datetime(2019, 12, 4)
end = datetime.datetime(2020, 12, 4)

apple = pdr.get_data_yahoo('AAPL', start, end)

# print(apple.describe())

# print(apple.tail())


# Plot the closing prices for `aapl`
prices = apple['Close']
apple['Close'].plot(grid=True)

plt.show()


# Shows daily percentage change in the adjusted close price.
daily_close = apple[['Adj Close']]
daily_pct_change = daily_close.pct_change()
daily_pct_change.fillna(0, inplace=True)

# print(daily_pct_change)

daily_log_returns = np.log(daily_close.pct_change()+1)

# print(daily_log_returns)


# Calculate the volatility of the given stock
min_periods = 75
volume = daily_pct_change.rolling(min_periods).std() * np.sqrt(min_periods)

volume.plot(figsize=(10, 8))

# plt.show()

# Find important minima and maxima of the high
N = 1  # number of iterations
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
plt.show()

# Another way to find the most important minima and maxima
# Find first important minimum or maximum
R = 1.05
all_highs = apple['High']
all_lows = apple['Low']
n = len(apple['High'])
min_and_max_values = []
print(len(all_highs))
print(len(all_lows))

def find_first():
    imin = 1
    imax = 1
    i = 2
    while i < n and all_lows[i] / all_lows[imin] < R and all_highs[imax] / all_highs[i] < R:
        if all_lows[i] < all_lows[imin]:
            imin = i
        if all_highs[i] > all_highs[imax]:
            imax = i
        i = i+1

    if imin < imax:
        print(all_lows[imin])
        print(imin)
        min_and_max_values.append(all_lows[imin])
    else:
        print(all_highs[imax])
        print(imax)
        min_and_max_values.append(all_highs[imax])

    return i


# FIND-MINIMUM(i)  Find the first important minimum after the ith point.


def find_minimum(i):
    imin = i

    while i < n and all_lows[i]/all_lows[imin] < R:
        if all_lows[i] < all_lows[imin]:
            imin = i
        i = i+1
    if i < n and all_lows[imin] < all_lows[i]:
        print(all_lows[imin])
        print(imin)
        min_and_max_values.append(all_lows[imin])

    return i


# FIND-MAXIMUM(i)  Find the first important maximum after the ith point.


def find_maximum(i):
    imax = i

    while i < (n-1) and all_highs[imax]/all_highs[i] < R:
        if all_highs[i] > all_highs[imax]:
            imax = i
        i = i+1

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


# Trying to find the symmetrical triangle breakout
for i in range(len(min_and_max_values)-3):
    if min_and_max_values[i] > min_and_max_values[i+2] and min_and_max_values[i+1] < min_and_max_values[i+3]:
        print("----------------------------")
        print(min_and_max_values[i])
        print(min_and_max_values[i+1])
        print(min_and_max_values[i+2])
        print(min_and_max_values[i+3])
        plt.plot(min_and_max_values)
        plt.show()
    elif min_and_max_values[i] < min_and_max_values[i+2] and min_and_max_values[i+1] > min_and_max_values[i+3]:
        print("----------------------------")
        print(min_and_max_values[i])
        print(min_and_max_values[i+1])
        print(min_and_max_values[i+2])
        print(min_and_max_values[i+3])
        plt.plot(min_and_max_values)
        plt.show()

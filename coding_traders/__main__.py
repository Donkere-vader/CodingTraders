from .signal import SignalDetector


class CodingTraders:
    def __init__(self):
        self.signaldetector = SignalDetector()

    def start(self):
        stockinformation_apple = self.signaldetector.get_stock_data("AAPL")
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
                # prints values i to i + 3 of list min_anx_max_values
                print("\n".join([str(min_and_max_values[i + j]) for j in range(0, 4)]))

            elif min_and_max_values[i] < min_and_max_values[i + 2] and min_and_max_values[i + 1] > \
                    min_and_max_values[i + 3]:
                print("----------------------------")
                # prints values i to i + 3 of list min_anx_max_values
                print("\n".join([str(min_and_max_values[i + j]) for j in range(0, 4)]))

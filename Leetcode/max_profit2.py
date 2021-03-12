INF = int(1e9)

class Solution:
    def maxProfit(self, prices):

        min_value = INF
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < min_value:
                min_value = prices[i]

            elif prices[i] - min_value > max_profit:
                max_profit = prices[i] - min_value

        return max_profit
from collections import deque


class Solution:
    def maxProfit(self, prices):

        profit = 0

        while 1:

            max_idx = prices.index(max(prices))
            min_idx = prices.index(min(prices))

            # 최소값과 최대값이 순서대로 있다면
            if min_idx <= max_idx:
                if profit < prices[max_idx] - prices[min_idx]:
                    profit = prices[max_idx] - prices[min_idx]
                break
            # 최대최소가 역순이라면,
            else:
                temp = prices[:max_idx + 1]

                if profit < (temp[-1] - min(temp)):
                    profit = temp[-1] - min(temp)

                prices = prices[max_idx + 1:]
        return profit


s = Solution()
print(s.maxProfit([2,4,1]))
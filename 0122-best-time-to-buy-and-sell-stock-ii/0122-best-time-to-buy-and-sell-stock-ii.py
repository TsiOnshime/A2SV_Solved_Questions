class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        sell = 1
        if sell > len(prices):
            return 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit += (prices[sell] - prices[buy])
                sell += 1
                buy += 1
            else:
                buy += 1
                sell += 1
        return profit
# sell = 1
# len(prices) = 6
# 1, 2
# profit = 4
# 2, 3
# 3, 4
# profit = 7
# 4, 5
# 5, 6

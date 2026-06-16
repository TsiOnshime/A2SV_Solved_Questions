class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy = 0, 1, 2
        n = len(prices)

        dp = [[[float('-inf')] * 3 for _ in range(2)] for _ in range(n)]


        def calculateProfit(i, buy, t):
            if i == n:
                return 0
            if t == 2:
                return 0
            if dp[i][buy][t] != float('-inf'):
                return dp[i][buy][t]

            if buy:
                profit = max(-prices[i] + calculateProfit(i + 1, 0, t), calculateProfit(i + 1, 1, t))
            else:
                profit = max(prices[i] + calculateProfit(i + 1, 1, t + 1), calculateProfit(i + 1, 0, t))

            dp[i][buy][t] = profit
            return profit
        return calculateProfit(0, 1, 0)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
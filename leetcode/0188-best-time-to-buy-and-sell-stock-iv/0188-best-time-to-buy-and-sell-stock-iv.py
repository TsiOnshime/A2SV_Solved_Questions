class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # t = 0, 1, 2, 3, 4
        #     b. s. b. s. b
        n = len(prices)
        dp = [[float('-inf')] * (2 * k) for _ in range(len(prices))]
        def calcProfit(i, t):
            if i == n:
                return 0
            if t == 2 * k:
                return 0
            if dp[i][t] != float('-inf'):
                return dp[i][t]

            if t % 2 == 0:
                profit = max(-prices[i] + calcProfit(i + 1, t + 1), calcProfit(i + 1, t))
            else:
                profit = max(prices[i] + calcProfit(i + 1, t + 1), calcProfit(i + 1, t))
            dp[i][t] = profit
            return profit
        return calcProfit(0, 0)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy = 0, 1, 2
        n = len(prices)

        dp = [[[float('-inf')] * 3 for _ in range(2)] for _ in range(n + 1)]

        for i in range(n+1):
            for j in range(2):
                dp[i][j][2] = 0
        for j in range(2):
            for k in range(2):
                dp[n][j][k] = 0

        for i in range(n - 1, -1, -1):
            for j in range(2):
                for k in range(2):
                    if j:
                        profit = max(-prices[i] + dp[i + 1][0][k], dp[i + 1][1][k])
                    else:
                        profit = max(prices[i] + dp[i + 1][1][k + 1], dp[i + 1][0][k])
                    dp[i][j][k] = profit
        
        return dp[0][1][0]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
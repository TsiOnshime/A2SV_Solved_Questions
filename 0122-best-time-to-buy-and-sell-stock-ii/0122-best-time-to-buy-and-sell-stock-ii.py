class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1 -> Buy
        dp = [[float('-inf')] * 2 for _ in range(len(prices) + 1)]
        for i in range(2):
            dp[len(prices)][i] = 0
        for i in range(len(prices) - 1, -1, -1):
            for j in range(2):
                profit = 0
                if j:
                    profit = max(-prices[i] + dp[i + 1][0], dp[i + 1][1])
                else:
                    profit = max(prices[i] + dp[i + 1][1], dp[i + 1][0])
                
                dp[i][j] = profit

        return dp[0][1]
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
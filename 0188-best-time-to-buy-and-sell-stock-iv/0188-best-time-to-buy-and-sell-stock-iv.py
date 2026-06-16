class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        n = len(prices)
        dp = [[[0] * (k + 1) for _ in range(2)] for i in range(len(prices) + 1)]

        for i in range(len(prices) - 1, -1, -1):
            for j in range(2):
                for l in range(1,k + 1):
                    if j:
                        profit = max(-prices[i] + dp[i + 1][0][l], dp[i + 1][1][l])
                    else:
                        profit = max(prices[i] + dp[i + 1][1][l - 1], dp[i + 1][0][l])
                    
                    dp[i][j][l] = profit
        return dp[0][1][k]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
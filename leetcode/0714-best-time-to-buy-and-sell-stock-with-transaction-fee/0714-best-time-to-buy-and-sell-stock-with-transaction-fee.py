class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[float('-inf')] * 2 for _ in range(n)]

        def calcProfit(i, b):
            if i == n:
                return 0
            if dp[i][b] != float('-inf'):
                return dp[i][b]

            if b:
                profit = max(-prices[i] + calcProfit(i + 1, 0), calcProfit(i + 1, 1))
            else:
                profit = max(prices[i] - fee + calcProfit(i + 1, 1), calcProfit(i + 1, 0))
            dp[i][b] = profit
            
            return profit

        return calcProfit(0, 1)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[float('-inf')] * (2) for _ in range(2)] for _ in range(n)]
        def calcProfit(i, b, c):
            if i == n:
                return 0
            if c:
                return calcProfit(i + 1, b, 0)
            if dp[i][b][c] != float('-inf'):
                return dp[i][b][c]

            if b:
                profit = max(-prices[i] + calcProfit(i + 1, 0, c), calcProfit(i + 1, 1, c))
            else:
                profit = max(prices[i] + calcProfit(i + 1, 1, 1), calcProfit(i + 1, 0, c))
            dp[i][b][c] = profit 
            return profit
        
        return calcProfit(0, 1, 0)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
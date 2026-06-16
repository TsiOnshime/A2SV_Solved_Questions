class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        n = len(prices)
        dp = [[[float('-inf')] * (k + 1) for _ in range(2)] for i in range(len(prices))]

        def calcProfit(i, buy, t):
            if  i == n:
                return 0
            if t == 0:
                return 0
            if dp[i][buy][t] != float('-inf'):
                return dp[i][buy][t]

            if buy:
                profit = max(-prices[i] + calcProfit(i + 1, 0, t), calcProfit(i + 1, 1, t))
            else:
                profit = max(prices[i] + calcProfit(i + 1, 1, t - 1), calcProfit(i + 1, 0, t))
            dp[i][buy][t] = profit
            return profit
        
        return calcProfit(0, 1, k)



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
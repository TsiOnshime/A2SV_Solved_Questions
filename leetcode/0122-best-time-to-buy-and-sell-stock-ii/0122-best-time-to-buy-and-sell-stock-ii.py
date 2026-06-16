class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1 -> Buy
        dp = [[float('-inf')] * 2 for _ in range(len(prices))]
        print(dp)
        def calc(i, buy):
            if i == len(prices):
                return 0
            if dp[i][buy] != float('-inf'):
                return dp[i][buy]

            if buy:
                profit = max(-prices[i] + calc(i + 1, 0), 0 + calc(i + 1, 1))

            else:
                profit = max(prices[i] + calc(i + 1, 1), 0 + calc(i + 1, 0))
            dp[i][buy] = profit
            
            return profit

        



        return calc(0, 1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
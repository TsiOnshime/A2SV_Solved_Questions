class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        _min = prices[0]
        profit = 0
        for i in range(len(prices)):
            cost = prices[i] - _min
            profit = max(profit, cost)

            _min = min(_min, prices[i])

        return profit

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
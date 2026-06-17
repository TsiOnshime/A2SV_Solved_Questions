class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        front = [0] * 2
        curr = [0] * 2

        for i in range(n - 1, -1, -1):
            for j in range(2):
                if j:
                    profit = max(-prices[i] + front[0], front[1])
                else:
                    profit = max(prices[i] - fee + front[1], front[0])

                curr[j] = profit
            front = curr.copy()
        return front[1]



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
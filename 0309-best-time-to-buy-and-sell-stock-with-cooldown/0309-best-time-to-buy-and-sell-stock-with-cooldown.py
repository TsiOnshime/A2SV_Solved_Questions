class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        front = [0] * 2
        curr = [0] * 2
        frontahead = 0

        for i in range(n - 1, -1, -1):
            for j in range(2):
                if j:
                    profit = max(-prices[i] + front[0], front[1])
                else:
                    if i + 2 <= n:
                        profit = max(prices[i] + frontahead, front[0])
                    else:
                        profit = max(prices[i],front[0])
                curr[j] = profit
            frontahead = front[1]
            front = curr.copy()
        return front[1]



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
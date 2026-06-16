class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy = 0, 1, 2
        n = len(prices)

        front = [[0] * 3 for _ in range(2)] 



        for i in range(n - 1, -1, -1):
            curr = [[0] * 3 for _ in range(2)]
            for j in range(2):
                for k in range(2):
                    if j:
                        profit = max(-prices[i] + front[0][k], front[1][k])
                    else:
                        profit = max(prices[i] + front[1][k + 1], front[0][k])

                    curr[j][k] = profit
            front = [row[:] for row in curr]
        return front[1][0]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
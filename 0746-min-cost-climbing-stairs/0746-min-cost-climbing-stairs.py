class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        c1, c2 = cost[0], cost[1]
        for i in range(2, len(cost)):
            _min = min(c1, c2)
            c1, c2 = c2, _min + cost[i]

        return min(c1, c2)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna
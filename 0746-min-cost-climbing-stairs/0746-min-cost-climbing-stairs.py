class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cache = {}

        def calc_min_cost(i):
            if i == 0:
                return cost[i]
            if i == 1:
                return cost[i]
            if i in cache:
                return cache[i]
            if i == len(cost):
                val = min(calc_min_cost(i - 1), calc_min_cost(i - 2))
            else:
                val = min(calc_min_cost(i - 1), calc_min_cost(i - 2)) + cost[i]
            cache[i] = val
            return val

        return calc_min_cost(len(cost))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna
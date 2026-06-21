class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        j = len(cuts) - 1
        cuts.insert(0, 0)
        cuts.append(n)
        cuts.sort()
        m = len(cuts)
        dp = [[-1] * m for _ in range(m)]
        def cutMin(i, j):
            if i > j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            min_cost = float('inf')
            for k in range(i, j + 1):
                op = cuts[j + 1] - cuts[i - 1] + cutMin(i, k - 1) + cutMin(k + 1, j)
                min_cost = min(min_cost, op)

            dp[i][j] = min_cost
            return min_cost
        
        return cutMin(1, len(cuts) - 2)
            


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
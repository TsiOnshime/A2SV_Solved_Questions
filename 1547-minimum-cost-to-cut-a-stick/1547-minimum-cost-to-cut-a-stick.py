class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.insert(0, 0)
        cuts.append(n)
        cuts.sort()
        m = len(cuts)
        
        dp = [[0] * (m + 2) for _ in range(m + 2)]
        
        for i in range(m - 2 , 0, -1):
            for j in range(1,m - 1):
                if i > j:
                    continue
                min_cost = float('inf')
                for k in range(i, j + 1):
                    op = cuts[j + 1] - cuts[i - 1] + dp[i][k - 1] + dp[k + 1][j]
                    min_cost = min(min_cost, op)
                dp[i][j] = min_cost
        
        return dp[1][m -2]
 
            


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
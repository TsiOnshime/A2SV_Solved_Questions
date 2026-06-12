class Solution:
    def knapSack(self, val, wt, capacity):

        dp = [[float('-inf')] * (capacity + 1) for _ in range(len(val))]

        def getItem(i, w):
            
            if i == 0:
                return (w//wt[0]) * val[0]
            if dp[i][w] != float('-inf'):
                return dp[i][w]
                
            notake = 0 + getItem(i - 1, w)
            
            take = float('-inf')
            if wt[i] <= w:
                take = val[i] + getItem(i, w - wt[i])
                
            value = max(notake, take)
            dp[i][w] = value
            return value
            
        return getItem(len(wt) - 1, capacity)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution:
    def knapSack(self, val, wt, capacity):

        dp = [[float('-inf')] * (capacity + 1) for _ in range(len(val))]

        # def getItem(i, w):
            
        #     if i == 0:
        #         return (w//wt[0]) * val[0]
        #     if dp[i][w] != float('-inf'):
        #         return dp[i][w]
                
        #     notake = 0 + getItem(i - 1, w)
            
        #     take = float('-inf')
        #     if wt[i] <= w:
        #         take = val[i] + getItem(i, w - wt[i])
                
        #     value = max(notake, take)
        #     dp[i][w] = value
        #     return value
            
        # return getItem(len(wt) - 1, capacity)
        
        for i in range(capacity + 1):
            dp[0][i] = (i //wt[0]) * val[0]
            
        for i in range(1, len(wt)):
            for j in range(capacity + 1):
                notake = 0 + dp[i - 1][j]
                take = float('-inf')
                if wt[i] <= j:
                    take = val[i] + dp[i][j - wt[i]]
                    
                dp[i][j] = max(notake, take)
                
        return dp[len(wt) - 1][capacity]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
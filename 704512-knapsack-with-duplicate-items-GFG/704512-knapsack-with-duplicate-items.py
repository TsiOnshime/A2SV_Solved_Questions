class Solution:
    def knapSack(self, val, wt, capacity):

        prev = [float('-inf')] * (capacity + 1)
        
        for i in range(capacity + 1):
            prev[i] = (i //wt[0]) * val[0]
            
        for i in range(1, len(wt)):
            for j in range(capacity + 1):
                notake = 0 + prev[j]
                take = float('-inf')
                if wt[i] <= j:
                    take = val[i] + prev[j - wt[i]]
                    
                prev[j] = max(notake, take)
 
        return prev[capacity]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
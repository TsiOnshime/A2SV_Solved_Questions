class Solution:
    def knapsack(self, W, val, wt):
        


        prev = [0] * (W + 1)

        

        for i in range(W + 1):
            if wt[0] <= i:
                prev[i] = val[0]
                
        for i in range(1, len(wt)):
            for j in range(W, -1, -1):
                nosteal = prev[j]
                steal = float('-inf')
                if wt[i] <= j:
                    steal = val[i] + prev[j - wt[i]]
                
                prev[j] = max(steal, nosteal)
                
        return prev[W]
                    
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
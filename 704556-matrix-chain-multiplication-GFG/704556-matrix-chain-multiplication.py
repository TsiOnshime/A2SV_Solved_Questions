class Solution:
    def matrixMultiplication(self, arr):
        # code here
        
        dp = [[-1] * len(arr) for _ in range(len(arr))]
        
        for i in range(len(arr)):
            dp[i][i] = 0
        
        for i in range(len(arr) - 1, 0, -1):
            for j in range(i + 1, len(arr)):
                _min = float('inf')
                for k in range(i, j):
                    steps = arr[i - 1] * arr[k] * arr[j] + dp[i][k] + dp[k + 1][j]
                    _min = min(steps, _min)
                    
                dp[i][j] = _min
        return dp[1][len(arr) - 1]
        
        def multiply(i, j):
            if i == j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
                
            min_operations = float('inf')
            for k in range(i, j):
                steps = arr[i - 1] * arr[k] * arr[j] + multiply(i, k) + multiply(k + 1, j)
                min_operations = min(steps, min_operations)
                
            dp[i][j] = min_operations
            return min_operations
        
        return multiply(1, len(arr) - 1)
        
        
                
                
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
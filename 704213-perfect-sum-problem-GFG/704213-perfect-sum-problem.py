#User function Template for python3
class Solution:
	def perfectSum(self, arr, target):


		dp = [[0] * (target + 1) for i in range(len(arr) + 1)]

    
        dp[len(arr)][target] = 1
            
        for i in range(len(arr) - 1, -1, -1):
            for j in range(target, -1, -1):
                notake = dp[i + 1][j]
                take = 0
                if j + arr[i] <= target:
                    take = dp[i + 1][j + arr[i]]
                dp[i][j] = take + notake
                
                
        return dp[0][0]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
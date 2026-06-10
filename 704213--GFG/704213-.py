#User function Template for python3
class Solution:
	def perfectSum(self, arr, target):
	    n = len(arr)
	    dp = [[0] * (target + 1) for i in range(n)]
        
        if arr[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1
        
        if arr[0] != 0 and arr[0] <= target:
            dp[0][arr[0]] = 1
	    
	    for i in range(1, n):
	        for j in range(target + 1):
	            notake = dp[i - 1][j]
	            take = 0
	            if arr[i] <= j:
	                take = dp[i- 1][j - arr[i]]
	            dp[i][j] = take + notake
	    return dp[n - 1][target]
	    
        
#         arr = [1,2,3]
# target = 4

#         0 1 2 3 4

# i=0    ? ? ? ? ?
# i=1    ? ? ? ? ?
# i=2    ? ? ? ? 1
# i=3    0 0 0 0 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
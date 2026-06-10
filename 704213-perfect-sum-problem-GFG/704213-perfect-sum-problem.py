#User function Template for python3
class Solution:
	def perfectSum(self, arr, target):
	    n = len(arr)
	    dp = [[-1] * (target + 1) for i in range(n)]
	    def countSubset(i, target):
	        nonlocal dp

	        if i == 0:
                if target == 0 and arr[0] == 0:
	                return 2
	            if arr[0] == target:
	                return 1
	            if target == 0:
	                return 1
	            return 0
	        if dp[i][target] != -1:
	            return dp[i][target]
	        
            notake = countSubset(i - 1, target)
            take = 0
            if arr[i] <= target:
                take = countSubset(i - 1, target - arr[i])
            dp[i][target] = take + notake
            return take + notake
            

        return countSubset(n - 1, target)

        
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
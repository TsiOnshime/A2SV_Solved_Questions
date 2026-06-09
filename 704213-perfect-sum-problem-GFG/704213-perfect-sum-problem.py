#User function Template for python3
class Solution:
	def perfectSum(self, arr, target):


		dp = [[-1] * (target + 1) for i in range(len(arr))]
		def countSubsets(i, _sum):
		    nonlocal dp
		    if _sum > target:
		        return 0
            if i == len(arr):
                return 1 if _sum == target else 0
            
            if dp[i][_sum] != -1:
                return dp[i][_sum]
                
            
            num = arr[i]
            
            take = countSubsets(i + 1, _sum + num)
            notake = countSubsets(i + 1, _sum)
            
            val = take + notake
            
            dp[i][_sum] = val
            return val
            
            
        return countSubsets(0, 0)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
#User function Template for python3
class Solution:
	def perfectSum(self, arr, target):
	    n = len(arr)
	    prev = [0] * (target + 1)
        
        if arr[0] == 0:
            prev[0] = 2
        else:
            prev[0] = 1
        
        if arr[0] != 0 and arr[0] <= target:
            prev[arr[0]] = 1
	    curr = [0] * (target + 1)
	    for i in range(1, n):
	        for j in range(target + 1):
	            notake = prev[j]
	            take = 0
	            if arr[i] <= j:
	                take = prev[j - arr[i]]
	            curr[j] = take + notake
	            
	        prev = curr.copy()
	    return prev[target]
	    
        
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
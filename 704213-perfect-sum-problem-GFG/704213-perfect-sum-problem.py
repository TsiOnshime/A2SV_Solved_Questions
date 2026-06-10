#User function Template for python3
class Solution:
	def perfectSum(self, arr, target):


		front= [0] * (target + 1) 

    
        front[target] = 1
        curr = [0] * (target + 1)
        for i in range(len(arr) - 1, -1, -1):
            for j in range(target + 1):
                notake = front[j]
                take = 0
                if j + arr[i] <= target:
                    take = front[j + arr[i]]
                curr[j] = take + notake
                
            front = curr.copy()
        return front[0]
        
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
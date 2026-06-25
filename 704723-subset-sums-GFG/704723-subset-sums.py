class Solution:
	def subsetSums(self, arr):
		# code here
		res = []
		n = len(arr)
		def calculateSum(i, _sum):
		    if i == n:
		        res.append(_sum)
		        return 
		    
		    # no take
		    calculateSum(i + 1, _sum)
		    
		    # take
		    calculateSum(i + 1, _sum + arr[i])

		calculateSum(0, 0)
		return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
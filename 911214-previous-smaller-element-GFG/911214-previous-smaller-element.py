class Solution:
	def prevSmaller(self, arr):
		# code here
		pse = [-1] * len(arr)
		stack = []
		
		for i in range(len(arr)):
		    while stack and stack[-1] >= arr[i]:
		        stack.pop()
		    pse[i] = stack[-1] if stack else -1
		    stack.append(arr[i])
		return pse

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
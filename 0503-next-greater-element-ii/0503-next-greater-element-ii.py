class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nge = [-1] * len(nums)
        stack = []

        for i in range(len(nums) - 1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            stack.append(nums[i])

        for i in range(len(nums) - 1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            nge[i] = stack[-1] if stack else -1
            stack.append(nums[i])
        return nge
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
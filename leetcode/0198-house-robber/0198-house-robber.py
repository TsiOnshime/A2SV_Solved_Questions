class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

# [6,3,10,8,2,10,3,5,10,5,3]
#                         i
# h1 = 36, h2 = 37
# h1 = 6, 
        h1, h2 = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
  
            h1, h2 = h2, max(h2, h1 + nums[i])

        return h2

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev2 = nums[0]
        prev = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            curr = max(prev, nums[i] + prev2)
            prev2 = prev
            prev = curr
        
        return prev

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna
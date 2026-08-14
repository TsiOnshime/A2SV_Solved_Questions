class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _max = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i - 1] + nums[i])
            _max = max(nums[i], _max)
        return _max

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
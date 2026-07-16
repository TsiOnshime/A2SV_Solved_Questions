class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        _sum = 0
        l, r = 0, 0
        min_length = float('inf')

        while r < len(nums):
            _sum += nums[r]
            while _sum - nums[l] >= target:
                _sum -= nums[l]
                l += 1
            if _sum >= target:
                min_length = min(min_length, r - l + 1)
            r += 1
      
    
      
        return min_length if min_length != float('inf') else 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
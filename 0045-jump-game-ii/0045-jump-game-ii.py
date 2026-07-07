class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        current_end = 0
        farthest = 0
        if len(nums) <= 1:
            return 0
        i = 0
        while i < len(nums):
            while i <= current_end:
                farthest = max(farthest, i + nums[i])
                i += 1
            current_end = farthest
            jump += 1
            if current_end >= len(nums) - 1:
                return jump


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
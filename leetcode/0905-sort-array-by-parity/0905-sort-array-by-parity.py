class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1

        while l <= r:
            while l < len(nums) and nums[l] % 2 == 0:
                l += 1
            while r >= 0 and nums[r] % 2:
                r -= 1
            if l < r and l < len(nums) and r >= 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        return nums

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
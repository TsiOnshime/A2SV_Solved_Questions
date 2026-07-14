class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        length = 0

        while r < len(nums):
            if nums[r] == 0:
                k -= 1
            while k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
            length = max(length, r - l + 1)
            r += 1
        return length

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
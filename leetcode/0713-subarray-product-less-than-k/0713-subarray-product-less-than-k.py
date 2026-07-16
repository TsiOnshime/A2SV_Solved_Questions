class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        product = 1
        count = 0
        l, r = 0, 0

        while r < len(nums):
            product *= nums[r]
            while product > k:
                product //= nums[l]
                l += 1
            if product < k:
                count += (r - l + 1)
            r += 1
        return count


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
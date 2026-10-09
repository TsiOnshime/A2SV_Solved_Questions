class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
       
        l, r = 1, 1

        while r < len(nums):
            if nums[r] == nums[l - 1]:
                r += 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1
        return l

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = mid = 0
        h = len(nums) - 1

        while mid <= h:
            if nums[mid] == 0:
                nums[l], nums[mid] = nums[mid], nums[l]
                mid += 1
                l += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[h] = nums[h], nums[mid]
                h -= 1
        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna
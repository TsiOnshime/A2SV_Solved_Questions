class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
       # the core idea is how to know if a number is appearing for the first time 
       # if nums[l - 1] == nums[r] it means the number at r is not the first time it is appearing so we move r pointer looking for the first unique number
       # if the number at r is appearing for the first time what we need to do is swap the duplicated element at l with the unique number at r and move both pointers
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
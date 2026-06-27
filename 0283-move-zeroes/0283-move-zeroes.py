class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_nums = []
        for i in range(len(nums)):
            if nums[i] != 0:
                new_nums.append(nums[i])
        
        for i in range(len(nums)):
            if i < len(new_nums):
                nums[i] = new_nums[i]
            else:
                nums[i] = 0
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
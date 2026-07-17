class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # change all negatives, zeros, and numbers greater than n to 1
        containsOnes = False
        for i in range(len(nums)):
            if nums[i] == 1:
                containsOnes = True
            elif nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = 1
        if not containsOnes: return 1

        # change the index where an element belongs to negative
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0: nums[index] = -nums[index]
        
        # search for the first index which is positive
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        return len(nums) + 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        groupA = 0 # rightMost = 1
        groupB = 0 # rightMost = 0

        num = 0
        for i in range(len(nums)):
            num ^= nums[i]
        
        rightMost = (num & (num - 1)) ^ num
        
        for i in range(len(nums)):
            if nums[i] & rightMost == 0:
                groupB ^= nums[i]
            else: 
                groupA ^= nums[i]
        
        return [groupA, groupB]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
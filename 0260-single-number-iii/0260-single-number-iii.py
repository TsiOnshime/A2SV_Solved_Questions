class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for i in range(len(nums)):
            xor ^= nums[i]
        
        rightMost = xor & -xor

        groupA = 0
        groupB = 0

        for i in range(len(nums)):
            if nums[i] & rightMost:
                groupA ^= nums[i]
            else:
                groupB ^= nums[i]
        
        return [groupA, groupB]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
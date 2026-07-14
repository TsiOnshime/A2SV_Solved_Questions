class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r = 0, 0
        length = 0
        # [1, 1, 0, 1, 1, 1]
        #          l       r
        
        while r < len(nums):
            if nums[r] != 0:
                length = max(length, r - l + 1)
            else:
                l = r + 1
            r += 1
        return length 

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
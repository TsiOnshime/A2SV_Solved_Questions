class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        l = 0
        r = 1

        length = 1

        while r < len(nums):
            if nums[r] <= nums[r - 1]:
                l = r
                
            length = max(length, r - l + 1)
            
            r += 1
        return length
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
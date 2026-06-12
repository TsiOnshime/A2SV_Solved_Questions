class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elem = 0
        count = 0

        for i in range(len(nums)):
            if count == 0:
                elem = nums[i]
                count = 1
            elif elem == nums[i]:
                count += 1
            else:
                count -= 1
        
        return elem

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
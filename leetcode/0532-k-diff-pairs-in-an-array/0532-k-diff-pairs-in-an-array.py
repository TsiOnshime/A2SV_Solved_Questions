class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        if len(nums) == 1:
            return 0
        print(nums)
        i, j = 0, 1
        count = 0

        while i < len(nums) and j < len(nums):
            while i < len(nums) and i > 0 and nums[i] == nums[i -1]:
                i += 1
            while j < len(nums) and j > 1 and nums[j] == nums[j - 1] and i != j - 1:
                j += 1
            if i < len(nums) and j < len(nums):
                diff = nums[j] - nums[i]
                if diff == k:
                    if i != j:
                        
                        count += 1
                    j += 1
                elif diff > k:
                    i += 1
                elif diff < k:
                    j += 1
        return count
    
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna